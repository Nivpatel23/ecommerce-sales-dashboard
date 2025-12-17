#  Power BI Dashboard Building Guide - E-commerce Sales

Complete step-by-step tutorial for creating a professional Power BI dashboard from scratch.

---

##  What You'll Build

A **4-page interactive Power BI dashboard** featuring:

- **Page 1:** Executive Overview (KPIs, trends, top-level metrics)
- **Page 2:** Product Analysis (category performance, product details)
- **Page 3:** Customer Insights (demographics, regional analysis)
- **Page 4:** Time Analysis (trends, patterns, forecasting)

**Total Time:** 2-3 hours for first build

---

##  Prerequisites

Before you start:

-  Power BI Desktop installed ([Download Free](https://powerbi.microsoft.com/desktop/))
-  CSV file ready: `ecommerce_sales_data.csv`
-  Basic understanding of data visualization
-  Windows 10/11 (Power BI Desktop is Windows-only)

---

##  PART 1: Import & Prepare Data

### Step 1.1: Open Power BI Desktop

1. Launch **Power BI Desktop**
2. Close the splash screen (or explore templates if interested)
3. You'll see a blank canvas

### Step 1.2: Import CSV Data

1. Click **Get Data** button (Home tab, left side)
2. Select **Text/CSV** from the list
3. Click **Connect**
4. Browse to find `ecommerce_sales_data.csv`
5. Click **Open**

### Step 1.3: Preview Data

Power BI shows a preview window with your data:

```
Order_ID | Date       | Year | Category    | Total_Sales | ...
ORD1000  | 2023-01-15 | 2023 | Electronics | 234.99      | ...
ORD1001  | 2023-01-15 | 2023 | Clothing    | 45.50       | ...
```

**Check:**
-  All columns visible
-  Data looks correct
-  No obvious errors

Click **Transform Data** to open Power Query Editor

### Step 1.4: Clean & Transform Data

In **Power Query Editor**:

**Check Data Types** (very important!):

1. Look at the column headers - they show icons indicating data type
2. Verify these data types:

| Column | Should Be | Icon | How to Fix |
|--------|-----------|------|------------|
| Order_ID | Text | ABC | Right-click → Change Type → Text |
| Date | Date/Time | Date | Right-click → Change Type → Date/Time |
| Year | Whole Number | 123 | Right-click → Change Type → Whole Number |
| Month_Num | Whole Number | 123 | Right-click → Change Type → Whole Number |
| Total_Sales | Decimal Number | 1.2 | Right-click → Change Type → Decimal Number |
| Unit_Price | Decimal Number | 1.2 | Right-click → Change Type → Decimal Number |
| Quantity | Whole Number | 123 | Right-click → Change Type → Whole Number |

**Common Issue:**
If Date shows as Text (ABC icon):
1. Right-click **Date** column
2. Select **Change Type** → **Date/Time**
3. Power BI will convert it

### Step 1.5: Rename Table (Optional but Recommended)

1. Look at left sidebar in Power Query
2. You'll see your table name (probably `ecommerce_sales_data`)
3. Right-click the table name
4. Select **Rename**
5. Type: `Sales` (shorter is better for formulas)
6. Press Enter

### Step 1.6: Load Data into Power BI

1. Click **Close & Apply** (top-left, big button)
2. Power BI loads your data
3. Wait 5-10 seconds for 18,500 rows to load
4. You're now back at the main canvas

 **Success!** Your data is now in Power BI and ready for analysis.

---

##  PART 2: Create DAX Measures

**What are DAX Measures?**
- Formulas that calculate values dynamically
- Like Excel formulas, but more powerful
- Recalculate based on filters and slicers

**Where to Create Them:**
- Right sidebar → Fields pane
- Find your table (Sales)
- Right-click on it → **New Measure**

### Step 2.1: Create Basic Measures

**Measure 1: Total Revenue**

1. Right-click **Sales** table (in Fields pane)
2. Select **New Measure**
3. In the formula bar at top, type:

```dax
Total Revenue = SUM(Sales[Total_Sales])
```

4. Press **Enter**
5.  You'll see "Total Revenue" appear under Sales table with ƒₓ icon

**Measure 2: Total Orders**

1. Right-click **Sales** table again
2. Select **New Measure**
3. Type:

```dax
Total Orders = COUNTROWS(Sales)
```

4. Press **Enter**

**Measure 3: Average Order Value**

1. Right-click **Sales** → **New Measure**
2. Type:

```dax
Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
```

3. Press **Enter**

**Why DIVIDE()?** It handles division by zero safely. The `0` at the end means "show 0 if you try to divide by zero."

**Measure 4: Total Quantity**

```dax
Total Quantity = SUM(Sales[Quantity])
```

**Measure 5: Unique Customers**

```dax
Unique Customers = DISTINCTCOUNT(Sales[Customer_ID])
```

 **Checkpoint:** You should now have 5 measures under your Sales table, all with ƒₓ icons.

### Step 2.2: Create Time Intelligence Measures

**Measure 6: Previous Year Revenue**

```dax
Previous Year Revenue = 
CALCULATE(
    [Total Revenue],
    DATEADD(Sales[Date], -1, YEAR)
)
```

**What it does:** Calculates revenue from same period last year.

**Measure 7: Year-over-Year Growth %**

```dax
YoY Growth % = 
DIVIDE(
    [Total Revenue] - [Previous Year Revenue],
    [Previous Year Revenue],
    0
) * 100
```

**Measure 8: Month-to-Date Revenue**

```dax
MTD Revenue = 
CALCULATE(
    [Total Revenue],
    DATESMTD(Sales[Date])
)
```

**Measure 9: Year-to-Date Revenue**

```dax
YTD Revenue = 
CALCULATE(
    [Total Revenue],
    DATESYTD(Sales[Date])
)
```

### Step 2.3: Create Advanced Measures

**Measure 10: Items Per Order**

```dax
Items Per Order = DIVIDE([Total Quantity], [Total Orders], 0)
```

**Measure 11: Revenue Per Customer**

```dax
Revenue Per Customer = DIVIDE([Total Revenue], [Unique Customers], 0)
```

**Measure 12: High Value Orders (>$200)**

```dax
High Value Orders = 
CALCULATE(
    [Total Orders],
    FILTER(Sales, Sales[Total_Sales] > 200)
)
```

**Measure 13: Previous Month Revenue**

```dax
Previous Month Revenue = 
CALCULATE(
    [Total Revenue],
    DATEADD(Sales[Date], -1, MONTH)
)
```

**Measure 14: Month-over-Month Growth %**

```dax
MoM Growth % = 
DIVIDE(
    [Total Revenue] - [Previous Month Revenue],
    [Previous Month Revenue],
    0
) * 100
```

**Measure 15: 3-Month Rolling Average**

```dax
3M Rolling Avg = 
CALCULATE(
    [Total Revenue],
    DATESINPERIOD(Sales[Date], LASTDATE(Sales[Date]), -3, MONTH)
) / 3
```

 **All Measures Created!** You should now have 15 measures ready to use.

---

##  PART 3: Build Page 1 - Executive Overview

### Step 3.1: Set Up Page

1. Look at bottom of screen - you'll see "Page 1"
2. Right-click on "Page 1" → **Rename**
3. Type: `Executive Overview`
4. Press Enter

### Step 3.2: Add KPI Cards (Top Row)

**Card 1: Total Revenue**

1. Click blank canvas
2. In Visualizations pane (right side), click **Card** icon (looks like a card with number)
3. From Fields pane, drag **Total Revenue** measure to the **Fields** well
4. Resize card by dragging corners
5. Position at top-left

**Format the Card:**
1. Click on card to select it
2. In Visualizations pane, click **Format** (paint roller icon)
3. Expand **Callout value**
4. Change font size to **32** or **36**
5. Make it **Bold**

**Repeat for Cards 2-4:**

**Card 2: Total Orders**
- Add measure: `Total Orders`
- Position: Top, next to Card 1

**Card 3: Average Order Value**
- Add measure: `Average Order Value`
- Position: Top, next to Card 2

**Card 4: Unique Customers**
- Add measure: `Unique Customers`
- Position: Top, next to Card 3

**Add Card Labels:**
1. For each card, turn on **Category label**
2. Format → Callout value → Category label → **On**
3. The measure name will show as a label

### Step 3.3: Add Monthly Sales Trend (Line Chart)

1. Click blank area on canvas (below KPI cards)
2. Select **Line chart** visual from Visualizations pane
3. Resize to be wide (take up ~60% of row width)

**Configure the chart:**
- **X-axis:** Drag `Date` field → Expand to Month hierarchy
- **Y-axis:** Drag `Total Revenue` measure
- **Legend:** Drag `Year` field (to compare 2023 vs 2024)

**Format the chart:**
1. Select chart → Format pane
2. **Title:**
   - Turn **On**
   - Text: "Monthly Sales Trend"
   - Font size: **14-16**
3. **Data labels:** Turn **On** (optional, can be cluttered)
4. **Legend:** Position → **Bottom**

### Step 3.4: Add Revenue by Category (Donut Chart)

1. Click blank area
2. Select **Donut chart** from Visualizations
3. Position: Right side of line chart

**Configure:**
- **Legend:** Drag `Category` field
- **Values:** Drag `Total Revenue` measure

**Format:**
1. **Title:** "Revenue Distribution by Category"
2. **Detail labels:** Turn **On**
3. **Category** and **Percentage** both visible

**Custom Colors (Optional):**
1. Format → Data colors
2. Assign specific colors to each category:
   - Electronics: Blue (#667eea)
   - Clothing: Pink (#f5576c)
   - Home & Garden: Green (#43e97b)
   - Sports: Purple (#f093fb)
   - Books: Light Blue (#4facfe)

### Step 3.5: Add Regional Performance (Bar Chart)

1. Click blank area (below line chart)
2. Select **Clustered bar chart**
3. Resize to medium width

**Configure:**
- **Y-axis:** Drag `Region` field
- **X-axis:** Drag `Total Revenue` measure

**Format:**
- **Title:** "Sales Performance by Region"
- **Data labels:** Turn **On**, Position → **Inside End**
- **Sort:** Click "..." → Sort descending by Total Revenue

### Step 3.6: Add Top 10 Products (Horizontal Bar)

1. Click blank area
2. Select **Clustered bar chart**
3. Position: Next to Regional Performance

**Configure:**
- **Y-axis:** Drag `Product` field
- **X-axis:** Drag `Total Revenue` measure

**Filter to Top 10:**
1. Select the visual
2. In Filters pane (right side), find **Product** filter
3. Change filter type to **Top N**
4. Set: Show items → **Top 10** → By value → **Total Revenue**
5. Click **Apply filter**

**Format:**
- **Title:** "Top 10 Best-Selling Products"
- **Data labels:** On
- **Sort:** Descending (should already be sorted)

### Step 3.7: Add Slicers

**Year Slicer:**
1. Click blank area (left sidebar is good spot)
2. Select **Slicer** from Visualizations
3. Drag `Year` field to the slicer

**Format:**
- Style → **Dropdown** (saves space)
- Or **Tile** if you prefer buttons

**Quarter Slicer:**
1. Add another slicer below Year
2. Drag `Quarter` field

**Category Slicer:**
1. Add another slicer
2. Drag `Category` field
3. Style → **Dropdown**

**Region Slicer:**
1. Add another slicer
2. Drag `Region` field
3. Style → **Dropdown**

 **Page 1 Complete!** You now have a professional executive overview page.

---

##  PART 4: Build Page 2 - Product Analysis

### Step 4.1: Create New Page

1. At bottom, click **+** icon to add new page
2. Rename it: `Product Analysis`

### Step 4.2: Add Product Performance Table

1. Select **Table** visual
2. Make it wide (take up ~60% of top area)

**Add columns:**
- Drag `Product` to Values
- Drag `Category` to Values (shows which category each product belongs to)
- Drag `Total Revenue` measure
- Drag `Total Quantity` measure
- Drag `Total Orders` measure

**Format:**
1. **Title:** "Product Performance Matrix"
2. **Conditional formatting** on Total Revenue:
   - Click on Total Revenue column
   - Format → Conditional formatting → Data bars → On
   - Color: Green gradient

### Step 4.3: Add Category Trend Line Chart

1. Select **Line chart**
2. Position: Right side of table

**Configure:**
- **X-axis:** `Date` (Month hierarchy)
- **Y-axis:** `Total Revenue`
- **Legend:** `Category`

**Format:**
- **Title:** "Category Performance Over Time"
- **Legend:** Bottom
- Multiple colored lines showing each category

### Step 4.4: Add Price vs Quantity Scatter Plot

1. Select **Scatter chart**
2. Position: Below table

**Configure:**
- **X-axis:** `Unit_Price`
- **Y-axis:** `Quantity`
- **Legend:** `Category`
- **Size:** `Total Revenue` (makes bubbles different sizes)

**Format:**
- **Title:** "Price vs Quantity Analysis"
- Shows relationship between price and volume

 **Page 2 Complete!**

---

##  PART 5: Build Page 3 - Customer Insights

### Step 5.1: Create New Page

1. Add new page (click + at bottom)
2. Rename: `Customer Insights`

### Step 5.2: Add Demographics Bar Chart

1. Select **Stacked bar chart**
2. Make it medium-large size

**Configure:**
- **Y-axis:** `Age_Group`
- **X-axis:** `Total Revenue`
- **Legend:** `Gender`

**Format:**
- **Title:** "Sales by Age Group and Gender"
- **Data labels:** On
- Shows which demographics spend most

### Step 5.3: Add Regional Distribution

1. Select **Clustered column chart**
2. Position: Next to demographics chart

**Configure:**
- **X-axis:** `Region`
- **Y-axis:** `Total Revenue` and `Unique Customers` (add both)

**Format:**
- **Title:** "Regional Customer Distribution"
- **Legend:** On (shows which bar is revenue, which is customers)

### Step 5.4: Add Customer Metrics Cards

Add 3 KPI cards at top:

**Card 1:** `Unique Customers`  
**Card 2:** `Revenue Per Customer`  
**Card 3:** `Items Per Order`

### Step 5.5: Add Region × Category Matrix

1. Select **Matrix** visual
2. Position: Bottom section

**Configure:**
- **Rows:** `Region`
- **Columns:** `Category`
- **Values:** `Total Revenue`

**Format:**
- **Conditional formatting:** Background color (heat map)
- Shows which categories perform best in which regions

 **Page 3 Complete!**

---

##  PART 6: Build Page 4 - Time Analysis

### Step 6.1: Create New Page

1. Add new page
2. Rename: `Time Analysis`

### Step 6.2: Add YoY Comparison Chart

1. Select **Clustered column chart**
2. Make it large width

**Configure:**
- **X-axis:** `Month`
- **Y-axis:** `Total Revenue`
- **Legend:** `Year`

**Format:**
- **Title:** "Year-over-Year Monthly Comparison"
- Side-by-side bars comparing 2023 vs 2024

### Step 6.3: Add Day of Week Pattern

1. Select **Column chart**
2. Position: Below YoY chart

**Configure:**
- **X-axis:** `Day_of_Week`
- **Y-axis:** `Total Orders`

**Sort Properly:**
1. Click "..." on visual
2. Sort by → `Day_of_Week`
3. Manually ensure it's Mon, Tue, Wed, Thu, Fri, Sat, Sun order

**Format:**
- **Title:** "Orders by Day of Week"
- Shows which days are busiest

### Step 6.4: Add Quarterly Performance

1. Select **Clustered column chart**

**Configure:**
- **X-axis:** `Quarter`
- **Y-axis:** `Total Revenue`
- **Legend:** `Year`

**Format:**
- **Title:** "Quarterly Performance 2023 vs 2024"

### Step 6.5: Add Growth Indicators

Add 2 KPI cards at top:

**Card 1:** `YoY Growth %`
- Format as percentage
- Add conditional formatting (green if positive)

**Card 2:** `MoM Growth %`
- Format as percentage

 **Page 4 Complete!**

---

##  PART 7: Formatting & Polish

### Step 7.1: Apply Consistent Theme

1. Go to **View** tab
2. Click **Themes**
3. Choose a professional theme (e.g., "Executive")
4. Or create custom theme:
   - View → Themes → Customize current theme
   - Set consistent colors across all pages

### Step 7.2: Format All Measures as Currency

1. Select any measure (e.g., Total Revenue)
2. Go to **Measure tools** tab (appears when measure selected)
3. **Format:** Dropdown → Choose **$ English (United States)**
4. **Decimals:** Set to **0** for whole dollars
5. Repeat for: Total Revenue, Average Order Value, Revenue Per Customer

### Step 7.3: Format Percentages

1. Select `YoY Growth %` measure
2. **Format:** Percentage
3. **Decimals:** 1
4. Repeat for `MoM Growth %`

### Step 7.4: Sync Slicers Across Pages

1. Go to **View** tab
2. Click **Sync slicers**
3. Pane opens on right
4. Select **Year slicer**
5. Check boxes for all pages where you want it to work
6. Repeat for other slicers

### Step 7.5: Add Page Navigation

**Option 1: Buttons**
1. Insert → Buttons → Blank
2. Format button with page name
3. Action → Type → Page navigation → Select page
4. Repeat for each page

**Option 2: Use built-in page navigation**
- Users can click page tabs at bottom (easier!)

### Step 7.6: Final Touches

**For ALL visuals across ALL pages:**

1. **Consistent Sizing:**
   - Align visuals using guidelines (View → Gridlines → Show)
   - Snap to grid (View → Snap to grid)

2. **Professional Titles:**
   - Every chart should have descriptive title
   - Font size: 14-16pt
   - Bold

3. **Data Labels:**
   - Turn on for KPIs and key charts
   - Turn off if cluttered

4. **Colors:**
   - Consistent across pages
   - Use theme colors

5. **White Space:**
   - Don't cram too much on one page
   - Leave breathing room

---

##  PART 8: Testing & Validation

### Step 8.1: Test Interactivity

**Cross-Filtering:**
1. Click on a bar in any chart
2. Other visuals should filter automatically
3. If not working: Select visual → Format → Edit interactions

**Slicers:**
1. Select different years
2. All charts should update
3. Select different categories
4. Relevant charts should filter

### Step 8.2: Validate Numbers

**Quick Check:**
1. Does Total Revenue make sense? (~$2.8M expected)
2. Does Total Orders = 18,542?
3. Does AOV = ~$151?
4. Do percentages add to 100%?

**Common Issues:**
- Numbers too high: Check if you're double-counting
- Numbers too low: Check filters applied
- Blanks showing: Check data types

### Step 8.3: Check Performance

**Load Times:**
- Each visual should load in <2 seconds
- If slow: Simplify visuals, reduce data

**Interactions:**
- Filters should apply instantly
- Slicers should be responsive

---

##  PART 9: Save & Export

### Step 9.1: Save Your Work

1. **File** → **Save As**
2. Name: `Ecommerce_Dashboard.pbix`
3. Save in your project folder: `powerbi/`
4. **Important:** Save frequently!

### Step 9.2: Export to PDF

1. **File** → **Export to PDF**
2. Choose: **Current Page** or **All Pages**
3. Save as: `Ecommerce_Dashboard.pdf`
4. Use this for presentations or portfolio

### Step 9.3: Take Screenshots

**For GitHub/Portfolio:**

1. Go to each page
2. **View** → **Fit to Page** (for best view)
3. Windows: **Win + Shift + S** (snipping tool)
4. Mac: **Cmd + Shift + 4**
5. Save as:
   - `dashboard_overview.png`
   - `product_analysis.png`
   - `customer_insights.png`
   - `time_analysis.png`

---

##  Final Checklist

Before considering your dashboard complete:

### Data & Measures
- [ ] All 15 measures created and working
- [ ] Measures formatted (currency, percentage)
- [ ] No #ERROR or BLANK values showing
- [ ] Numbers make logical sense

### Page 1: Executive Overview
- [ ] 4 KPI cards at top
- [ ] Monthly trend line chart
- [ ] Category donut chart
- [ ] Regional bar chart
- [ ] Top 10 products chart
- [ ] Slicers working

### Page 2: Product Analysis
- [ ] Product performance table
- [ ] Category trend chart
- [ ] Price vs quantity scatter
- [ ] All data labels clear

### Page 3: Customer Insights
- [ ] Demographics chart
- [ ] Regional distribution
- [ ] Customer KPI cards
- [ ] Region × Category matrix

### Page 4: Time Analysis
- [ ] YoY comparison chart
- [ ] Day of week pattern
- [ ] Quarterly performance
- [ ] Growth indicators

### Formatting & Polish
- [ ] Consistent colors across all pages
- [ ] All charts have titles
- [ ] Theme applied
- [ ] Slicers synced across pages
- [ ] Cross-filtering working
- [ ] Professional appearance

### Files & Documentation
- [ ] .pbix file saved
- [ ] PDF exported
- [ ] Screenshots taken
- [ ] Ready to upload to GitHub

---

##  Troubleshooting

### Issue: Measure Shows #ERROR

**Problem:** Formula has syntax error

**Solution:**
```dax
# Check for common mistakes:
 Total Revenue = SUM(Sales Total_Sales)      # Missing brackets
 Total Revenue = SUM(Sales[Total_Sales])     # Correct

 Average Order Value = [Total Revenue] / [Total Orders]  # No error handling
 Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)  # Safe
```

### Issue: Date Filters Not Working

**Problem:** Date column is Text, not Date type

**Solution:**
1. Go to Power Query (Home → Transform Data)
2. Right-click Date column
3. Change Type → Date/Time
4. Close & Apply

### Issue: Slicer Doesn't Filter Charts

**Problem:** Visual interaction disabled

**Solution:**
1. Select the slicer
2. Format → Edit interactions (appears in ribbon)
3. Click on charts that should be filtered
4. Ensure filter icon (funnel) is selected, not "None"

### Issue: Numbers Look Wrong (Too High/Low)

**Problem:** Incorrect aggregation

**Solution:**
- Check if measure is SUM when it should be AVERAGE
- Verify COUNTROWS vs COUNT
- Look for duplicate rows in data

### Issue: Charts Load Slowly

**Problem:** Too much data or complex calculations

**Solution:**
1. Simplify visuals (fewer data points)
2. Remove unnecessary columns from data
3. Use aggregated data where possible
4. Check for circular dependencies in measures

---

##  Pro Tips

### Tip 1: Use Bookmarks for Presentation

Create bookmarks to save specific views:
1. View → Bookmarks → Add bookmark
2. Name it (e.g., "Q4 Focus")
3. Use during presentations to jump to key insights

### Tip 2: Add Tooltips

Create custom tooltip pages:
1. New page → Page Information → Set as Tooltip
2. Add mini-charts and KPIs
3. Apply to any visual for richer hover experience

### Tip 3: Use Field Parameters for Dynamic Visuals

Create visuals where users can switch between metrics:
1. Modeling → New Parameter → Fields
2. Select measures to include
3. Add parameter to chart
4. Users can toggle between Revenue, Orders, etc.

### Tip 4: Keyboard Shortcuts

- **Ctrl + C / Ctrl + V:** Copy/paste visuals
- **Ctrl + Z:** Undo
- **Ctrl + S:** Save
- **F11:** Full screen mode
- **Ctrl + Alt + V:** Paste and copy formatting

### Tip 5: Test on Different Screen Sizes

View → Phone Layout (create mobile-optimized version)

---

##  What You've Learned

By completing this dashboard, you've demonstrated:

**Technical Skills:**
-  Power BI Desktop proficiency
-  DAX formula creation (15+ measures)
-  Data modeling and transformation
-  Advanced visualization techniques
-  Interactive dashboard design
-  Time intelligence calculations

**Business Skills:**
-  KPI definition and tracking
-  Business intelligence strategy
-  Data storytelling
-  Insight generation
-  Executive reporting

---

##  Next Steps

### Immediate (After Completing This Guide)
1. Save your .pbix file
2. Export to PDF
3. Take screenshots
4. Upload all to GitHub

### Short-Term Enhancements
1. Add drill-through pages for detailed analysis
2. Create more complex DAX measures
3. Add conditional formatting
4. Build custom tooltips

### Long-Term Learning
1. Learn DAX advanced functions (CALCULATE, FILTER)
2. Explore Power Query M language
3. Study data modeling best practices
4. Practice with real datasets

---

##  Need Help?

**Common Resources:**
- [Official Power BI Documentation](https://docs.microsoft.com/power-bi/)
- [DAX Guide](https://dax.guide/) - Complete DAX function reference
- [SQLBI](https://www.sqlbi.com/) - Advanced DAX patterns
- [Power BI Community](https://community.powerbi.com/) - Forums and help

**YouTube Channels:**
- Guy in a Cube (Microsoft Power BI team)
- Curbal (Detailed tutorials)
- SQLBI (Advanced techniques)

---

##  Congratulations!

You've built a professional Power BI dashboard from scratch! This project showcases your ability to:
- Import and transform data
- Create complex DAX calculations
- Design intuitive visualizations
- Tell stories with data
- Build interactive, self-service analytics

**This dashboard is now ready for your portfolio!** 

---

**Guide Version:** 1.0  
**Last Updated:** December 2024  
**Compatible with:** Power BI Desktop (latest version)

**Created by:** Niv Patel    
**Contact:** nivwork23@gmail.com

---


