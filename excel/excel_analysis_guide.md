#  Excel Analysis Guide - E-commerce Sales

Complete step-by-step tutorial for analyzing e-commerce sales data using Excel pivot tables and formulas.

---

##  What You'll Create

A professional Excel workbook with **7 sheets** analyzing e-commerce data:

-  **Sheet 1:** Raw data (imported CSV)
-  **Sheet 2:** Sales by Category analysis
-  **Sheet 3:** Monthly Trends (2023 vs 2024)
-  **Sheet 4:** Regional Performance
-  **Sheet 5:** Customer Demographics
-  **Sheet 6:** Top 10 Products
-  **Sheet 7:** Executive Dashboard

---

##  STEP 1: Import Your Data

### 1.1 Open Excel and Create New Workbook

1. Launch Microsoft Excel
2. Click **File → New → Blank Workbook**
3. Save immediately: **File → Save As**
4. Name it: `Ecommerce_Sales_Analysis.xlsx`

### 1.2 Import CSV File

1. Go to **Data** tab in top ribbon
2. Click **Get Data → From File → From Text/CSV**
3. Browse and select `ecommerce_sales_data.csv`
4. Click **Import**

### 1.3 Load Data into Excel

Excel shows a preview window:
- Click **"Load"** button (NOT "Transform Data")
- Data appears in Sheet1 as a formatted table

 **Success!** You should see alternating row colors and filter buttons in headers.

### 1.4 Find Your Table Name (IMPORTANT!)

1. Click **any cell** in your data
2. Look for **"Table Design"** tab that appears at top
3. Click **Table Design** tab
4. Look at **Table Name** box (usually top-left)
5. Note the name - probably `Table1` or `ecommerce_sales_data`

** Write it down:** My table name is: `________________`

**You'll use this name in all formulas!** This guide uses `Table1` - replace with yours if different.

---

##  STEP 2: Create Sheet 2 - Sales by Category

### 2.1 Create PivotTable

1. Click **any cell** in your data (Sheet1)
2. Go to **Insert** tab → Click **PivotTable**
3. In dialog:
   - Table/Range should auto-fill
   - Select **"New Worksheet"**
4. Click **OK**

### 2.2 Rename the Sheet

1. Right-click on **"Sheet2"** tab (bottom of screen)
2. Select **"Rename"**
3. Type: `Category Analysis`
4. Press Enter

### 2.3 Build the PivotTable

You'll see a blank PivotTable on the left and field list on the right.

**STEP A: Add Category to Rows**
- Find **Category** in the field list (right side)
- Drag it down to the **Rows** box at bottom
- Your PivotTable now shows: Electronics, Clothing, Home & Garden, Sports, Books

**STEP B: Add Total Sales to Values**
- Find **Total_Sales** in the field list
- Drag it to the **Values** box
- Excel automatically adds "Sum of Total_Sales"
- Now you see dollar amounts next to each category!

**STEP C: Add Order Count**
- Find **Order_ID** in field list
- Drag it to **Values** box (below Total_Sales)
- Excel automatically counts orders
- Now you have two columns: Total Sales and Order Count

**Your PivotTable should look like:**
```
Row Labels      | Sum of Total_Sales | Count of Order_ID
Electronics     | 847200            | 2134
Clothing        | 412300            | 5234
Home & Garden   | 389100            | 3456
Sports          | 356800            | 2987
Books           | 145600            | 4731
```

### 2.4 Format as Currency

1. Right-click on **any sales number** in the PivotTable
2. Select **"Value Field Settings"**
3. Click **"Number Format"** button (bottom of dialog)
4. Choose **"Currency"** from category list
5. Set **Decimal places: 0** (for cleaner look)
6. Click **OK**, then **OK** again

 **Result:** Now shows **$847,200** instead of 847200

### 2.5 Add a Chart

1. Click **anywhere** in your PivotTable
2. Go to **Insert** tab → **PivotChart**
3. Choose **"Column Chart"** (first option)
4. Click **OK**

**Add Chart Title:**
1. Click on chart title text box
2. Type: `Sales Revenue by Product Category`
3. Press Enter

 **Sheet 2 Complete!** Professional category analysis with table and chart.

---

##  STEP 3: Create Sheet 3 - Monthly Trends

Follow same process as Sheet 2, but with different fields:

### 3.1 Create New PivotTable
1. Go back to Sheet1 (raw data)
2. Insert → PivotTable → New Worksheet
3. Rename sheet to: `Monthly Trends`

### 3.2 Build PivotTable

**Configuration:**
- **Rows:** `Year`, then `Month` (drag both, Year first)
- **Values:** `Total_Sales` (Sum), `Order_ID` (Count)

### 3.3 Insert Chart
- Chart type: **Line Chart**
- Title: `Monthly Sales Trend 2023-2024`

---

##  STEP 4: Create Sheet 4 - Regional Performance

### 4.1 Create New PivotTable
1. Sheet1 → Insert → PivotTable → New Worksheet
2. Rename: `Regional Analysis`

### 4.2 Build PivotTable

**Configuration:**
- **Rows:** `Region`
- **Columns:** `Category`
- **Values:** `Total_Sales` (Sum)

This creates a matrix showing sales by region AND category!

### 4.3 Insert Chart
- Chart type: **Clustered Bar Chart**
- Title: `Sales Performance by Region`

---

##  STEP 5: Create Sheet 5 - Customer Demographics

### 5.1 Create New PivotTable
1. Sheet1 → Insert → PivotTable → New Worksheet
2. Rename: `Demographics`

### 5.2 Build PivotTable

**Configuration:**
- **Rows:** `Age_Group`
- **Columns:** `Gender`
- **Values:** `Total_Sales` (Sum)

### 5.3 Insert Chart
- Chart type: **Stacked Column Chart**
- Title: `Sales by Age Group and Gender`

---

##  STEP 6: Create Sheet 6 - Top Products

### 6.1 Create New PivotTable
1. Sheet1 → Insert → PivotTable → New Worksheet
2. Rename: `Top Products`

### 6.2 Build PivotTable

**Configuration:**
- **Rows:** `Product`
- **Values:** `Total_Sales` (Sum), `Quantity` (Sum), `Order_ID` (Count)

### 6.3 Filter to Top 10

1. Click dropdown arrow next to "Row Labels"
2. Click **"Value Filters"** → **"Top 10..."**
3. Set: Top 10 items by Sum of Total_Sales
4. Click OK

### 6.4 Insert Chart
- Chart type: **Bar Chart** (horizontal bars)
- Title: `Top 10 Best-Selling Products`

---

##  STEP 7: Create Dashboard Sheet

### 7.1 Create New Sheet
1. Right-click sheet tabs → Insert → Worksheet
2. Rename: `Dashboard`

### 7.2 Add KPI Formulas

Set up layout like this:

| Cell | Label | Formula |
|------|-------|---------|
| A1 | Total Revenue | (label) |
| B1 | (formula) | `=SUM(Table1[Total_Sales])` |
| A2 | Total Orders | (label) |
| B2 | (formula) | `=COUNTA(Table1[Order_ID])` |
| A3 | Average Order Value | (label) |
| B3 | (formula) | `=AVERAGE(Table1[Total_Sales])` |
| A4 | 2024 Revenue | (label) |
| B4 | (formula) | `=SUMIFS(Table1[Total_Sales], Table1[Year], 2024)` |
| A5 | 2023 Revenue | (label) |
| B5 | (formula) | `=SUMIFS(Table1[Total_Sales], Table1[Year], 2023)` |
| A6 | YoY Growth % | (label) |
| B6 | (formula) | `=(B4-B5)/B5*100` |

** REPLACE `Table1` WITH YOUR ACTUAL TABLE NAME!**

### 7.3 Format Dashboard Cells

1. Select cells B1-B5
2. Press Ctrl+1 (opens Format Cells)
3. Choose Currency, 0 decimals
4. Click OK

For B6 (percentage):
1. Select B6
2. Press Ctrl+1
3. Choose Percentage, 1 decimal
4. Click OK

### 7.4 Copy Charts to Dashboard

1. Go to any analysis sheet (e.g., Category Analysis)
2. Click on chart to select it
3. Press Ctrl+C (copy)
4. Go to Dashboard sheet
5. Press Ctrl+V (paste)
6. Drag to position nicely
7. Repeat for 3-4 of your best charts

 **Arrange charts in a grid below your KPIs for professional look!**

---

##  Quick Reference - All Sheets

| Sheet Name | Rows | Columns | Values | Chart Type |
|------------|------|---------|--------|------------|
| **Category Analysis** | Category | (none) | Total_Sales, Order_ID | Column Chart |
| **Monthly Trends** | Year, Month | (none) | Total_Sales, Order_ID | Line Chart |
| **Regional Analysis** | Region | Category | Total_Sales | Bar Chart |
| **Demographics** | Age_Group | Gender | Total_Sales | Stacked Column |
| **Top Products** | Product (Top 10) | (none) | Total_Sales, Quantity, Order_ID | Bar Chart |
| **Dashboard** | (formulas) | (formulas) | (copied charts) | Multiple |

---

##  Final Checklist

Before considering your workbook complete:

- [ ] Sheet 1: Raw data imported and formatted as table
- [ ] Sheet 2: Category Analysis with PivotTable and Column Chart
- [ ] Sheet 3: Monthly Trends with PivotTable and Line Chart
- [ ] Sheet 4: Regional Analysis with PivotTable and Bar Chart
- [ ] Sheet 5: Demographics with PivotTable and Stacked Column Chart
- [ ] Sheet 6: Top Products with filtered PivotTable and Bar Chart
- [ ] Sheet 7: Dashboard with KPI formulas and copied charts
- [ ] All currency values formatted with $ symbol
- [ ] All charts have descriptive titles
- [ ] File saved as: `Ecommerce_Sales_Analysis.xlsx`

---

##  Troubleshooting

### Error: #NAME?

**Problem:** Formula doesn't recognize table name

**Solution:**
1. Check your table name (Table Design tab)
2. Replace `Table1` with your actual name in formulas
3. Names are case-sensitive!

Example:
```
 =SUM(Table1[Total_Sales])        ← If your table isn't named Table1
 =SUM(YourTableName[Total_Sales])  ← Use your actual name
```

### Error: #REF!

**Problem:** Column name doesn't exist or misspelled

**Solution:**
1. Check exact column spelling in your data
2. Look for underscores: `Total_Sales` not `Total Sales`
3. Column names are case-sensitive

### PivotTable Won't Create

**Problem:** Insert PivotTable is grayed out

**Solution:**
1. Make sure you clicked inside your data table
2. If data isn't a table yet: Select data, press Ctrl+T
3. Check "My table has headers", click OK
4. Try creating PivotTable again

### Formula Shows #DIV/0!

**Problem:** Dividing by zero

**Solution:**
Add error handling:
```
 =B4/B5
 =IFERROR(B4/B5, 0)
 =IF(B5=0, 0, B4/B5)
```

### Numbers Not Showing as Currency

**Solution:**
1. Select the cells
2. Press Ctrl+1
3. Choose Currency format
4. Set decimals to 0 or 2
5. Click OK

---

##  Pro Tips

### Tip 1: Use Slicers for Interactive Filtering

Add slicers to make your PivotTables interactive:
1. Click in PivotTable
2. PivotTable Analyze → Insert Slicer
3. Select fields like Year, Category, Region
4. Click OK
5. Use slicers to filter data interactively!

### Tip 2: Refresh Data

If you update your CSV file:
1. Data tab → Refresh All
2. All PivotTables update automatically!

### Tip 3: Conditional Formatting

Make your dashboard pop:
1. Select KPI cells
2. Home → Conditional Formatting → Data Bars
3. Choose green for positive metrics

### Tip 4: Name Your Ranges

Instead of cell references, name important cells:
1. Select cell B1 (Total Revenue)
2. Click in Name Box (top-left, shows cell address)
3. Type: `TotalRevenue`
4. Press Enter
5. Now use `=TotalRevenue` in other formulas!

---

##  Taking Screenshots for Portfolio

After completing your workbook:

1. **Dashboard Overview**: Capture entire Dashboard sheet (Ctrl+Shift+S on Windows)
2. **Category Chart**: Zoom to 100%, screenshot the chart
3. **Monthly Trend**: Capture the line chart showing 2-year comparison
4. **Regional Analysis**: Screenshot the bar chart
5. **Top Products**: Capture the top 10 products chart

**Save screenshots as:**
- `dashboard_overview.png`
- `category_chart.png`
- `monthly_trend.png`
- `regional_chart.png`
- `top_products.png`

Upload these to your GitHub repository in the `screenshots/` folder!

---

##  What You've Learned

By completing this analysis, you've demonstrated:

**Technical Skills:**
-  Data import and table formatting
-  PivotTable creation and configuration
-  Excel formulas (SUM, AVERAGE, SUMIFS, COUNTIF)
-  Chart creation and formatting
-  Dashboard design and layout

**Business Skills:**
-  Sales trend analysis
-  Category performance evaluation
-  Regional comparison
-  Customer segmentation
-  KPI tracking and reporting

---

## Next Steps

1. **Save your file**: Make sure all changes are saved
2. **Take screenshots**: Capture your best visuals
3. **Upload to GitHub**: Add file to your repository
4. **Update README**: Add Excel analysis section to project README
5. **Use for Power BI**: This analysis guides your Power BI dashboard design

---

##  Need Help?

Common questions:

**Q: Can I use Google Sheets instead?**
A: Yes, but PivotTable features differ slightly. Excel is recommended for this project.

**Q: My table has different columns - what do I do?**
A: Adapt the guide! Use the same process but with your column names. The concepts remain the same.

**Q: How long should this take?**
A: First time: 45-60 minutes. With practice: 20-30 minutes.

**Q: Do I need all 7 sheets?**
A: Minimum: Sheets 2, 3, 6, and 7. Others add depth but aren't mandatory.

---

**Last Updated:** December 2024  
**Excel Version:** Works with Excel 2016, 2019, 2021, Microsoft 365

---

**Good luck with your analysis! ** 
