#  Technical Documentation - E-commerce Sales Dashboard

## System Architecture Overview

This document provides comprehensive technical specifications for the e-commerce sales analytics dashboard, including data architecture, implementation details, and deployment procedures.

---

##  Data Architecture

### Data Flow Diagram

```
┌─────────────────┐
│  Python Script  │
│ (generate_data) │
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│  CSV File Export    │
│ (UTF-8, 18.5K rows) │
└────────┬────────────┘
         │
         ├──────────────────────────┐
         ▼                          ▼
┌─────────────────┐     ┌──────────────────┐
│  Excel Import   │     │  Power BI Import │
│  (Pivot Tables) │     │  (Power Query)   │
└─────────────────┘     └────────┬─────────┘
                                 │
                                 ▼
                        ┌──────────────────┐
                        │   Data Model     │
                        │   (Star Schema)  │
                        └────────┬─────────┘
                                 │
                                 ▼
                        ┌──────────────────┐
                        │   DAX Measures   │
                        │   (15+ KPIs)     │
                        └────────┬─────────┘
                                 │
                                 ▼
                        ┌──────────────────┐
                        │  Visualizations  │
                        │   (4 Pages)      │
                        └──────────────────┘
```

### Entity Relationship

**Single Table Model** (Flat Structure)

```
ecommerce_sales_data (Fact Table)
├── Order_ID (PK)
├── Date (Date dimension embedded)
├── Year
├── Month
├── Month_Num
├── Quarter
├── Day_of_Week
├── Category (Product dimension embedded)
├── Product
├── Unit_Price
├── Quantity
├── Total_Sales (Calculated: Unit_Price × Quantity)
├── Customer_ID (Customer dimension embedded)
├── Region
├── Age_Group
├── Gender
├── Payment_Method
└── Shipping_Method
```

**Normalization Level**: Denormalized (optimized for analytics)  
**Reason**: Single table simplifies queries and improves performance for BI workloads

---

##  Data Generation (Python)

### Technology Stack

- **Python**: 3.8+
- **Pandas**: 1.5.0+
- **NumPy**: 1.23.0+

### Script Architecture

```python
# generate_data.py structure

1. IMPORTS
   - pandas, numpy, datetime, random

2. CONFIGURATION
   - num_tickets = 18,542
   - date_range = 2023-01-01 to 2024-12-31
   - reference_data (categories, products, etc.)

3. GENERATION LOGIC
   - Loop through date range
   - Apply seasonal weights (Q4 boost)
   - Random product selection with category constraints
   - Price calculation with variance
   - Customer assignment (repeat buyers)

4. DATA QUALITY
   - Unique Order_IDs
   - No null values in required fields
   - Realistic distributions
   - Business hour constraints

5. EXPORT
   - CSV output (UTF-8)
   - Summary statistics
   - Data validation checks
```

### Key Algorithms

**Seasonal Adjustment**:
```python
def get_daily_orders(month):
    if month in [11, 12]:  # Holiday season
        return random.randint(40, 80)
    elif month in [7, 8]:  # Summer
        return random.randint(35, 65)
    else:
        return random.randint(20, 45)
```

**Price Variation**:
```python
def calculate_price(category, base_price):
    variance = random.uniform(0.8, 1.2)
    return round(base_price * variance, 2)
```

**Customer Behavior**:
```python
# Repeat customer logic
if random.random() < 0.42:  # 42% repeat rate
    customer_id = random.choice(existing_customers)
else:
    customer_id = generate_new_customer()
```

### Data Quality Checks

```python
# Validation performed after generation
assert df['Order_ID'].is_unique  # No duplicates
assert df['Total_Sales'].min() > 0  # All positive
assert df.isnull().sum().sum() == 0  # No nulls
assert df['Date'].min() >= '2023-01-01'  # Date range
assert df['Date'].max() <= '2024-12-31'
```

### Performance Metrics

- **Generation Time**: ~5-10 seconds for 18.5K records
- **Memory Usage**: ~50MB peak
- **Output File Size**: 2.5MB (CSV)
- **Optimization**: Vectorized operations, efficient data types

---

##  Power BI Implementation

### Data Import & Transformation

**Power Query Steps**:

1. **Source**
   ```m
   = Csv.Document(File.Contents("ecommerce_sales_data.csv"),
     [Delimiter=",", Encoding=65001])
   ```

2. **Promoted Headers**
   ```m
   = Table.PromoteHeaders(Source, [PromoteAllScalars=true])
   ```

3. **Changed Types**
   ```m
   = Table.TransformColumnTypes(#"Promoted Headers",{
       {"Order_ID", type text},
       {"Date", type datetime},
       {"Year", Int64.Type},
       {"Total_Sales", Currency.Type},
       ...
   })
   ```

4. **Date Table Creation** (Optional Enhancement)
   ```dax
   DateTable = 
   ADDCOLUMNS(
       CALENDAR(DATE(2023,1,1), DATE(2024,12,31)),
       "Year", YEAR([Date]),
       "Month", FORMAT([Date], "MMMM"),
       "Quarter", "Q" & FORMAT([Date], "Q"),
       "MonthNum", MONTH([Date])
   )
   ```

### Data Model

**Table**: ecommerce_sales_data
- **Rows**: 18,542
- **Columns**: 18
- **Size**: ~8MB in memory (compressed)
- **Refresh**: Manual (no data source connection)

**Relationships**: None required (single table)

**Sort Order**:
- Month sorted by Month_Num
- Day_of_Week sorted by custom list

### DAX Measures Library

#### Core Business Metrics

```dax
// Revenue Measures
Total Revenue = SUM(Sales[Total_Sales])

Previous Year Revenue = 
CALCULATE(
    [Total Revenue],
    DATEADD(Sales[Date], -1, YEAR)
)

YoY Growth % = 
DIVIDE(
    [Total Revenue] - [Previous Year Revenue],
    [Previous Year Revenue],
    0
) * 100

MTD Revenue = 
CALCULATE(
    [Total Revenue],
    DATESMTD(Sales[Date])
)

YTD Revenue = 
CALCULATE(
    [Total Revenue],
    DATESYTD(Sales[Date])
)
```

```dax
// Order Metrics
Total Orders = COUNTROWS(Sales)

Average Order Value = 
DIVIDE([Total Revenue], [Total Orders], 0)

Orders Last Year = 
CALCULATE(
    [Total Orders],
    DATEADD(Sales[Date], -1, YEAR)
)
```

```dax
// Customer Metrics
Unique Customers = DISTINCTCOUNT(Sales[Customer_ID])

Revenue Per Customer = 
DIVIDE([Total Revenue], [Unique Customers], 0)

Customers YoY Growth = 
VAR CurrentYear = [Unique Customers]
VAR PreviousYear = CALCULATE([Unique Customers], 
                              DATEADD(Sales[Date], -1, YEAR))
RETURN DIVIDE(CurrentYear - PreviousYear, PreviousYear, 0) * 100
```

```dax
// Product Metrics
Total Quantity = SUM(Sales[Quantity])

Items Per Order = 
DIVIDE([Total Quantity], [Total Orders], 0)

Average Unit Price = 
DIVIDE([Total Revenue], [Total Quantity], 0)
```

#### Advanced Analytics

```dax
// Moving Averages
3M Rolling Avg Revenue = 
CALCULATE(
    [Total Revenue],
    DATESINPERIOD(
        Sales[Date],
        LASTDATE(Sales[Date]),
        -3,
        MONTH
    )
) / 3

// Ranking
Product Revenue Rank = 
RANKX(
    ALL(Sales[Product]),
    [Total Revenue],
    ,
    DESC,
    DENSE
)

// Percentage of Total
Category % of Total = 
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALL(Sales[Category])),
    0
)
```

#### Conditional Calculations

```dax
// High Value Orders
High Value Orders = 
CALCULATE(
    [Total Orders],
    FILTER(Sales, Sales[Total_Sales] > 200)
)

// Top 10 Products Flag
Is Top 10 Product = 
IF([Product Revenue Rank] <= 10, "Yes", "No")

// Growth Indicator
Growth Status = 
SWITCH(
    TRUE(),
    [YoY Growth %] >= 20, " Excellent",
    [YoY Growth %] >= 10, " Good",
    [YoY Growth %] >= 0, " Stable",
    " Declining"
)
```

### Performance Optimization

**Query Performance**:
- Average visual load: <1 second
- Dashboard refresh: <3 seconds
- Full data refresh: <5 seconds

**Optimization Techniques**:
1. **DirectQuery vs. Import**: Import mode for better performance
2. **Aggregations**: Pre-calculated at category level
3. **Column Indexing**: Order_ID, Date indexed
4. **Remove Unused Columns**: Keep only necessary fields
5. **Data Types**: Appropriate types (Int vs. Decimal)

**Memory Management**:
```
Uncompressed size: 45MB
Compressed in memory: 8MB
Compression ratio: 5.6:1
```

---

##  Visualization Design

### Design System

**Color Palette**:
```
Primary: #667eea (Purple-Blue)
Secondary: #764ba2 (Purple)
Accent 1: #f5576c (Pink-Red)
Accent 2: #43e97b (Green)
Accent 3: #4facfe (Light Blue)
Neutral: #f5f5f5 (Light Gray)
Text: #333333 (Dark Gray)
```

**Typography**:
- **Titles**: Segoe UI Bold, 16-18pt
- **KPI Values**: Segoe UI Bold, 32-40pt
- **Data Labels**: Segoe UI, 10-12pt
- **Axis Labels**: Segoe UI, 9-10pt

**Layout Grid**:
- **Page Size**: 1920 × 1080 (16:9)
- **Margin**: 20px all sides
- **Gutter**: 20px between visuals
- **Column System**: 12-column grid

### Visual Selection Matrix

| Data Type | Best Visual | Alternative | Avoid |
|-----------|-------------|-------------|-------|
| **Single KPI** | Card | Gauge | Table |
| **Trend over Time** | Line Chart | Area Chart | Pie Chart |
| **Category Comparison** | Bar Chart | Column Chart | Radar |
| **Part-to-Whole** | Donut Chart | Treemap | Multiple Pie |
| **Distribution** | Histogram | Box Plot | Scatter |
| **Correlation** | Scatter Plot | Bubble Chart | Line |
| **Geographic** | Map | Choropleth | Table |
| **Ranking** | Bar Chart | Table | Pie |
| **Hierarchical** | Treemap | Sunburst | Stacked Bar |

### Interaction Design

**Cross-Filtering**:
```
Enabled Between:
- All charts on same page
- Slicers to all visuals
- Cards remain static (no filtering)

Disabled Between:
- Pages (independent contexts)
- Tooltip pages (no interaction)
```

**Drill-Through**:
```
From: Category (any chart)
To: Product Detail Page
Pass Filters: Category, Region, Date

From: Region (any chart)
To: Regional Deep Dive
Pass Filters: Region, Category
```

**Tooltips**:
```
Default: Show data point value + context
Custom: Mini dashboard with:
- Trend sparkline
- KPI comparison
- Relevant metrics
```

---

## Web Demo (HTML/JavaScript)

### Technology Stack

- **HTML5**: Structure
- **CSS3**: Styling (Flexbox, Grid)
- **JavaScript ES6**: Interactivity
- **Chart.js 3.9.1**: Data visualization

### Architecture

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Meta tags, title, Chart.js CDN -->
</head>
<body>
    <!-- Header Section -->
    <header>
        <h1>Dashboard Title</h1>
        <nav>Filters</nav>
    </header>
    
    <!-- KPI Cards Section -->
    <section class="kpi-grid">
        <div class="kpi-card">...</div>
    </section>
    
    <!-- Charts Section -->
    <section class="charts-grid">
        <canvas id="chart1"></canvas>
        <canvas id="chart2"></canvas>
    </section>
    
    <!-- Chart.js initialization scripts -->
    <script src="charts.js"></script>
</body>
</html>
```

### Chart Configuration

```javascript
// Example: Category Revenue Chart
const categoryChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books'],
        datasets: [{
            data: [847200, 412300, 389100, 356800, 145600],
            backgroundColor: ['#667eea', '#f5576c', '#43e97b', '#f093fb', '#4facfe']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom'
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return context.label + ': $' + context.parsed.toLocaleString();
                    }
                }
            }
        }
    }
});
```

### Responsive Design

```css
/* Mobile First Approach */
.charts-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
}

/* Tablet */
@media (min-width: 768px) {
    .charts-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Desktop */
@media (min-width: 1200px) {
    .charts-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

### Performance Optimization

- **Lazy Loading**: Charts render on scroll
- **Debouncing**: Filter changes debounced 300ms
- **Caching**: Data cached in sessionStorage
- **Minification**: CSS/JS minified for production
- **CDN**: Chart.js loaded from CloudFlare CDN

---

##  File Specifications

### CSV Export

**Encoding**: UTF-8  
**Delimiter**: Comma (,)  
**Line Endings**: CRLF (\r\n)  
**Quote Character**: Double quotes (")  
**Escape Character**: Backslash (\)  

**Header Row**: Yes (row 1)  
**Data Starts**: Row 2  
**Total Rows**: 18,543 (including header)  

**Column Data Types**:
```
Order_ID: String (8 chars, format: "ORD####")
Date: ISO 8601 (YYYY-MM-DD HH:MM:SS)
Year: Integer (4 digits)
Month: String (full month name)
Month_Num: Integer (1-12)
Quarter: String (Q1-Q4)
Day_of_Week: String (full day name)
Category: String (max 20 chars)
Product: String (max 30 chars)
Unit_Price: Decimal (2 decimals)
Quantity: Integer (1-8)
Total_Sales: Decimal (2 decimals)
Customer_ID: String (8 chars, format: "CUST####")
Region: String (max 10 chars)
Age_Group: String (5-7 chars)
Gender: String (max 10 chars)
Payment_Method: String (max 20 chars)
Shipping_Method: String (max 20 chars)
```

### Power BI File (.pbix)

**Version**: Compatible with Power BI Desktop (latest)  
**File Size**: 8-15 MB  
**Compression**: ZIP-based compression  
**Embedded Data**: Yes (Import mode)  

**Contents**:
- Data model (1 table)
- Measures (15+)
- Visualizations (4 pages, 20+ visuals)
- Themes and formatting
- Bookmarks (optional)

### Excel File (.xlsx)

**Version**: Excel 2016+ compatible  
**File Size**: 5-8 MB  
**Sheets**: 7 (Data + 5 Analysis + Dashboard)  

**Structure**:
```
Sheet1: Raw Data (Table)
Sheet2: Category Analysis (PivotTable + Chart)
Sheet3: Monthly Trends (PivotTable + Chart)
Sheet4: Regional Analysis (PivotTable + Chart)
Sheet5: Demographics (PivotTable + Chart)
Sheet6: Top Products (PivotTable + Chart)
Sheet7: Dashboard (Formulas + Charts)
```

---

##  Development Environment

### Local Setup

```bash
# Prerequisites
- Python 3.8+
- Power BI Desktop (free)
- Excel 2016+
- Modern web browser
- Git

# Clone Repository
git clone https://github.com/username/ecommerce-sales-dashboard.git
cd ecommerce-sales-dashboard

# Generate Data
cd scripts
pip install -r requirements.txt
python generate_data.py

# Output: ecommerce_sales_data.csv in /data folder
```

### Dependencies

**Python** (`requirements.txt`):
```
pandas>=1.5.0
numpy>=1.23.0
```

**Web Demo**:
```html
<!-- CDN Dependencies -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1"></script>
```

**No other dependencies required!**

---

##  Deployment

### GitHub Repository

**Repository Structure**:
```
ecommerce-sales-dashboard/
├── .gitignore
├── LICENSE (MIT)
├── README.md
├── data/
├── scripts/
├── excel/
├── powerbi/
├── screenshots/
├── docs/
└── demo/
```

**.gitignore** Contents:
```gitignore
# Power BI
*.pbix~
*.pbix.tmp

# Excel
~$*.xlsx
~$*.xls

# Python
__pycache__/
*.pyc
.venv/

# OS
.DS_Store
Thumbs.db

# Large files (optional)
# *.csv
```

### GitHub Pages Deployment

**Setup**:
1. Repository Settings → Pages
2. Source: `main` branch
3. Folder: `/demo`
4. Save

**URL**: `https://username.github.io/ecommerce-sales-dashboard/`

**Build Time**: 1-2 minutes  
**Deployment**: Automatic on push to main

---

##  Testing & Validation

### Data Quality Tests

```python
# Run after data generation
def validate_data(df):
    # Check 1: No nulls
    assert df.isnull().sum().sum() == 0, "Null values found"
    
    # Check 2: Unique Order IDs
    assert df['Order_ID'].is_unique, "Duplicate Order IDs"
    
    # Check 3: Positive sales
    assert (df['Total_Sales'] > 0).all(), "Negative sales found"
    
    # Check 4: Date range
    assert df['Date'].min() >= pd.Timestamp('2023-01-01'), "Date too early"
    assert df['Date'].max() <= pd.Timestamp('2024-12-31'), "Date too late"
    
    # Check 5: Calculated field accuracy
    assert ((df['Unit_Price'] * df['Quantity'] - df['Total_Sales']).abs() < 0.01).all(), \
        "Total_Sales calculation error"
    
    print(" All data quality checks passed")
```

### Dashboard Testing

**Functional Tests**:
- [ ] All measures calculate correctly
- [ ] Filters apply to visuals
- [ ] Charts render without errors
- [ ] Drill-through navigation works
- [ ] Tooltips display properly
- [ ] Export to PDF/PowerPoint functions

**Performance Tests**:
- [ ] Visual load time <2 seconds
- [ ] Filter response <1 second
- [ ] Full refresh <5 seconds
- [ ] No memory leaks on interaction

**Cross-Browser Tests** (Web Demo):
- [ ] Chrome 90+
- [ ] Firefox 88+
- [ ] Safari 14+
- [ ] Edge 90+

---

##  Monitoring & Maintenance

### Performance Metrics

**Key Indicators**:
- Dashboard load time
- Query response time
- Memory usage
- Visual rendering speed

**Benchmarks**:
- Excellent: <1 second
- Good: 1-2 seconds
- Acceptable: 2-3 seconds
- Needs optimization: >3 seconds

### Maintenance Schedule

**Weekly**:
- Monitor dashboard usage
- Check for errors/bugs
- Review user feedback

**Monthly**:
- Update documentation if changes made
- Optimize slow-performing queries
- Add new features if requested

**Quarterly**:
- Regenerate sample data with latest patterns
- Update dashboard design if needed
- Performance audit and optimization

---

##  Security Considerations

**Data Privacy**:
-  All data is synthetic (no real customer information)
-  No PII (Personally Identifiable Information)
-  Safe for public repository
-  No API keys or credentials in code

**Best Practices Followed**:
- No hardcoded paths
- No sensitive information in commits
- .gitignore configured properly
- Open source license (MIT)

---

##  Change Log

### Version 1.0 (December 2024)
- Initial release
- 18,542 transactions dataset
- Power BI dashboard (4 pages)
- Excel analysis workbook
- Web demo
- Complete documentation

### Planned Future Versions
- v1.1: Add predictive analytics
- v1.2: Real-time data refresh capability
- v1.3: Mobile-optimized layout
- v2.0: Interactive filtering on web demo

---

## Troubleshooting

### Common Issues

**Power BI: "Cannot connect to data source"**
- Solution: Check file path in Power Query
- Refresh data source settings
- Ensure CSV file exists in correct location

**Excel: Formula #NAME? error**
- Solution: Check table name in formula
- Verify table exists and is named correctly
- Ensure column names match exactly

**Web Demo: Charts not rendering**
- Solution: Check browser console for errors
- Verify Chart.js CDN is accessible
- Clear browser cache and reload

**Python: ModuleNotFoundError**
- Solution: Install requirements
- ```pip install pandas numpy```
- Verify Python version 3.8+

---

## Support & Contact

**General Inquiries**: nivwork23@gmail.com

**Documentation Version**: 1.0  
**Last Updated**: December 2024  
**Maintained By**: Niv Patel 

---

**This technical documentation provides the foundation for understanding, deploying, and maintaining the e-commerce sales dashboard project.**
