
# Monthly Sales Analysis — Data Science Project

### *A complete end-to-end data science workflow using NumPy, Pandas, Matplotlib, and Seaborn.*

---

##  1. Project Overview

This repository documents a complete data science workflow focused on analyzing **monthly sales performance** for a fictional company’s **four primary products** over the course of one year.

The objective is not just to display numbers — but to transform raw, synthetic data into **clear, actionable business recommendations**.

The project begins from scratch:  
No pre-existing data  
Data is generated programmatically  
Full analysis is done step-by-step

---

##  2. Technologies Used

This project relies on the core tools of the Python data science ecosystem:

- **Python** — Main programming language  
- **Pandas** — Data manipulation, metric calculations, pivot tables  
- **NumPy** — Efficient generation of synthetic random sales data  
- **Matplotlib** & **Seaborn** — Visualization tools for trends, heatmaps, boxplots  
- **Jupyter Notebook** — Interactive environment for analysis and documentation  

---

##  3. Project Structure

\`\`\`
project_sales/
│
├── notebook.ipynb        # The main analysis notebook (Steps 2–6)
├── utils.py              # Functions for data generation (Step 1)
│
└── data/
    ├── initial.csv       # Raw generated sales data
    ├── final.csv         # DataFrame with calculated metrics
    └── output.csv        # Final summary outputs (pivot tables, etc.)
\`\`\`

---

##  4. Key Steps & Analysis

### **Stage 1 — Data Generation & Preparation**

- Synthetic monthly sales generated using \`utils.py\`
- Products:
  - Product A  
  - Product B  
  - Product C  
  - Product D  
- Metrics computed:
  - **Total Monthly Sales**
  - **Average Sales**
  - **Month-over-Month Growth Rate**
- Feature Engineering:
  - Assigning each month to a business **Quarter (Q1–Q4)**

---

### **Stage 2 — Summarization & Insights**

- **Pivot Tables** to compute:
  - Average quarterly sales per product  
- Key insights extracted programmatically:
  -  **Best Product of the Year**
  -  **Best Month**
  -  **Best Quarter**

---

### **Stage 3 — Visualization & Conclusions**

--Visualizations were created using Matplotlib and Seaborn to explore sales trends, consistency, and distribution patterns:
.Line Charts—Show monthly sales trends for each product over 12 months.
  .Data is transformed into long format with melt() for Seaborn compatibility.
  .sns.lineplot() with hue='Product' separates product lines with different colors.
  .marker='o' adds markers for each month for better visibility.
.Boxplots + Swarmplots — Show performance consistency and identify outliers.
  .Boxplots display the median, interquartile range (IQR), and whiskers.
  .Swarmplots overlay individual sales points to show distribution variability.
  .Helps identify which products are stable (low variability) and which are inconsistent.
.Heatmap — Visualizes sales volume and density across months and products.
  .Data is transposed so products appear on the vertical axis and months on the horizontal axis.
  .annot=True displays the actual sales numbers on the heatmap.
  .Color palette (cmap='YlGnBu') helps quickly identify high and low sales months.
Key Insights from Visualizations:
 .Product A consistently outperforms others in median sales.
 .Q4 shows a clear seasonal peak for all products.
 .Product D has higher variability, indicating less consistent performance.
These visualizations help deliver clear, data-driven business recommendations, such as:
  .Increase marketing budget in Q4 to maximize seasonal demand.
  .Focus on stabilizing sales for Product D.
  .Consider mid-year promotions to boost sales in Q2.
##  5. How to Run the Project

### **1. Clone the Repository**
\`\`\`
git clone [Your Repository URL]
cd project_sales
\`\`\`

### **2. Install Dependencies**
Use Anaconda or pip to install:
- pandas
- numpy
- matplotlib
- seaborn
- jupyter

### **3. Generate Synthetic Data**
\`\`\`
python utils.py
\`\`\`
This automatically creates:
\`\`\`
data/initial.csv
\`\`\`

### **4. Run the Full Analysis**
\`\`\`
jupyter notebook notebook.ipynb
\`\`\`
Run all cells from top to bottom.

---

##  6. Results and Recommendations
*(This section will be filled after completing the analysis.)*

**Top Performer:** _[Product A]_  
**Seasonal Peak:** _[October–December]_  
**Recommendation:**  
 **Recommendations:
     .Increase marketing budget in Q4 to maximize seasonal demand.
     .Improve sales consistency for Product D.
     .Consider mid-year promotions in Q2 to boost sales.

##  7. Authors

**Yassine TALAHARI**  
**MESBAHI Abdullah**

EOF
