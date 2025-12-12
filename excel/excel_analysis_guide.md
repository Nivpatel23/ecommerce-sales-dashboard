<div class="success-box" style="margin-top: 20px;">
                    <span class="tip-icon">✅</span>
                    <strong>Dashboard Complete!</strong> Format cells B1-B6 as currency or percentage as needed (select cells, press Ctrl+1 for format menu).
                </div>
            </div>
        </div>
        
        <div class="step-box">
            <div class="step-header">
                <span class="step-number">3</span>
                Copy Charts from Other Sheets
            </div>
            <div class="step-content">
                <p>Make your dashboard visual by adding the best charts:</p>
                <ol style="margin-left: 20px; line-height: 2;">
                    <li>Go to <strong>Category Analysis</strong> sheet</li>
                    <li>Click on your chart to select it</li>
                    <li>Press <kbd>Ctrl</kbd> + <kbd>C</kbd> (copy)</li>
                    <li>Go back to <strong>Dashboard</strong> sheet</li>
                    <li>Press <kbd>Ctrl</kbd> + <kbd>V</kbd> (paste)</li>
                    <li>Drag to position it nicely</li>
                    <li>Repeat for other charts you want on dashboard</li>
                </ol>
                
                <div class="info-box" style="margin-top: 15px;">
                    <span class="tip-icon">💡</span>
                    <strong>Pro Tip:</strong> Copy 3-4 of your best charts to the dashboard. Arrange them in a grid below your KPI formulas for a professional look!
                </div>
            </div>
        </div>
    </div>
    
    <!-- FINAL CHECKLIST -->
    <div class="section">
        <div class="section-title">
            ✅ Final Checklist
        </div>
        
        <table>
            <thead>
                <tr>
                    <th>Sheet</th>
                    <th>Has PivotTable?</th>
                    <th>Has Chart?</th>
                    <th>Formatted?</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Sheet 1: Raw Data</td>
                    <td>N/A</td>
                    <td>N/A</td>
                    <td>✅ Imported</td>
                </tr>
                <tr>
                    <td>Sheet 2: Category Analysis</td>
                    <td>✅</td>
                    <td>✅ Column Chart</td>
                    <td>✅ Currency</td>
                </tr>
                <tr>
                    <td>Sheet 3: Monthly Trends</td>
                    <td>✅</td>
                    <td>✅ Line Chart</td>
                    <td>✅ Currency</td>
                </tr>
                <tr>
                    <td>Sheet 4: Regional Analysis</td>
                    <td>✅</td>
                    <td>✅ Bar Chart</td>
                    <td>✅ Currency</td>
                </tr>
                <tr>
                    <td>Sheet 5: Demographics</td>
                    <td>✅</td>
                    <td>✅ Stacked Column</td>
                    <td>✅ Currency</td>
                </tr>
                <tr>
                    <td>Sheet 6: Top Products</td>
                    <td>✅</td>
                    <td>✅ Bar Chart</td>
                    <td>✅ Currency</td>
                </tr>
                <tr>
                    <td>Sheet 7: Dashboard</td>
                    <td>N/A</td>
                    <td>✅ Copied charts</td>
                    <td>✅ Formulas work</td>
                </tr>
            </tbody>
        </table>
        
        <div class="success-box" style="margin-top: 20px;">
            <span class="tip-icon">🎉</span>
            <strong>Congratulations!</strong> You've created a professional Excel analysis workbook!<br><br>
            <strong>Next steps:</strong>
            <ul style="margin-left: 20px; margin-top: 10px;">
                <li>Save your file</li>
                <li>Take screenshots of your best charts</li>
                <li>Upload to GitHub repository</li>
                <li>Use this as reference for Power BI dashboard</li>
            </ul>
        </div>
    </div>
    
    <!-- TROUBLESHOOTING -->
    <div class="section">
        <div class="section-title">
            🆘 Common Issues & Solutions
        </div>
        
        <div class="warning-box">
            <h4 style="margin-bottom: 10px;">❌ Error: #NAME?</h4>
            <p><strong>Problem:</strong> Formula doesn't recognize table name</p>
            <p><strong>Solution:</strong></p>
            <ol style="margin-left: 20px; margin-top: 5px;">
                <li>Check your table name (Table Design tab)</li>
                <li>Replace <code>Table1</code> with your actual name</li>
                <li>Names are case-sensitive!</li>
            </ol>
        </div>
        
        <div class="warning-box">
            <h4 style="margin-bottom: 10px;">❌ Error: #REF!</h4>
            <p><strong>Problem:</strong> Column name doesn't exist</p>
            <p><strong>Solution:</strong></p>
            <ol style="margin-left: 20px; margin-top: 5px;">
                <li>Check exact column spelling</li>
                <li>Look for underscores: <code>Total_Sales</code> not <code>Total Sales</code></li>
                <li>Column names are case-sensitive</li>
            </ol>
        </div>
        
        <div class="warning-box">
            <h4 style="margin-bottom: 10px;">❌ PivotTable Won't Create</h4>
            <p><strong>Problem:</strong> Insert PivotTable is grayed out</p>
            <p><strong>Solution:</strong></p>
            <ol style="margin-left: 20px; margin-top: 5px;">
                <li>Make sure you clicked inside your data table</li>
                <li>Convert to table: Select data, press <kbd>Ctrl</kbd> + <kbd>T</kbd></li>
                <li>Try again</li>
            </ol>
        </div>
    </div>
</div>
