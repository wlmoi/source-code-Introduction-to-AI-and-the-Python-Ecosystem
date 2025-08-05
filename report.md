# AI Assignment Report - William Anthony
## goci 13223048@std.stei.itb.ac.id "Introduction to AI and the Python Ecosystem" ./WilliamAnthony_AI.zip
(English)

## PROBLEM STATEMENT / ASSIGNMENT
AI Assignment
1. Download the dataset on the 'Source Code' above.

2. Do some explorations through the dataset, including:
- Display the first 5 rows of the dataset.
- Display a concise summary of the dataset information.

3. Perform data analysis:
- Create a new column named Total_Pendapatan which is the result of multiplying Harga_Satuan by Jumlah_Terjual.
- Calculate and display the overall total revenue from all transactions.
- Find and display the product with the highest quantity sold.
- Calculate the total revenue for each product category.
- Filter and display transactions where the quantity sold is greater than 20.

4. Save the results:
- Create a new DataFrame containing the aggregated revenue per category.
- Save this new DataFrame to a CSV file named category_summary.csv. Do not include the row index in the saved CSV file.

5. Answer the following questions in a file named report.md 
- Based on the output of your Python script, write down several insights (minimum of 3) that you found. Example: "Which product category is the most profitable?"
- Briefly explain the differences between Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) based on your understanding from the module.
- Imagine you are a store owner. How can you leverage AI to improve your business based on the existing sales data? Provide a minimum of 2 examples of AI implementation and briefly explain how they work.

Task Provisions
- The task must be completed independently.
- Write down any assumptions if you feel something is ambiguous or unclear.
- All task code must be written in a python file or an ipynb notebook file.
- Also, add descriptions for the code or insights obtained in a separate markdown file or within a markdown cell in the ipynb file.
- Compress all submission files into a zip file with the naming format <Full Name>_AI.zip.



## ANSWER
## 1. Insights from Data Analysis

So, based of the output of the Python script (machine_learning.py) after processing `data_penjualan.csv` and the `category_summary.csv` file, here are several insights found:

*   **Overall Revenue:** The overall total revenue from all transactions was calculated to be **$738,000.00**. This figure provides a clear benchmark of the business's financial performance over the period covered by the dataset, indicating its overall scale of sales.

*   **Top-Selling Product by Quantity:** The product with the highest quantity sold was **'Air Mineral'** with **30 units sold**. This highlights 'Air Mineral' as a key volume driver for the business, suggesting its popularity among customers and potential for further marketing, which means stock prioritization.

*   **Most Profitable Category:** The **'Makanan'** product category generated the highest total revenue, amounting to **$283,500.00**. This indicates that 'Makanan' is the most profitable segment for the business, warranting strategic focus for growth, inventory management, and promotional activities. Following closely are 'Minuman' with $272,000.00 and 'Alat Tulis' with $182,500.00.

*   **High-Volume Transactions:** There were **3 transactions** where the quantity sold was greater than 20. These specific transactions involved 'Pensil 2B' (25 units), 'Air Mineral' (30 units), and 'Teh Botol' (22 units). These larger-volume transactions could represent bulk purchases, business-to-business sales, or popular items purchased in larger quantities by individual consumers. This suggests opportunities such as loyalty programs or specific large-volume customer targeting.



## 2. Differences Between Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL)

Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) are interconnected fields within computer science. They are often used interchangeably, but they represent distinct levels of complexity and scope.

*   **Artificial Intelligence (AI)** is the broadest concept. It refers to the development of computer systems that can perform tasks traditionally requiring human intelligence. These tasks include problem-solving, decision-making, understanding natural language, and perceiving environments. AI encompasses a wide array of techniques, from simple rule-based systems to highly complex learning algorithms. The ultimate goal is to enable machines to think and act like humans or at least act rationally.

*   **Machine Learning (ML)** is a subset of AI. ML focuses on developing algorithms that allow computers to "learn" from data without being explicitly programmed for every specific task. Instead of being given step-by-step instructions, ML models are trained on large datasets, enabling them to identify patterns, make predictions, or take decisions based on the learned patterns. Common ML applications include spam detection, recommendation systems, and predictive analytics.

*   **Deep Learning (DL)** is a specialized subset of ML. Deep Learning uses artificial neural networks with multiple layers (hence "deep") to learn complex patterns and representations from data. These deep neural networks are particularly effective with large amounts of unstructured data such as images, audio, and text. Unlike traditional ML, Deep Learning often reduces the need for manual "feature engineering" because the deep networks can automatically learn hierarchical features directly from the raw input. Deep Learning has driven significant advancements in areas like facial recognition, voice assistants, and autonomous driving.

In essence, AI is the overarching goal of creating intelligent machines. ML is one of the primary ways to achieve AI by enabling machines to learn from data. DL is a powerful, modern technique within ML that uses deep neural networks to handle complex data and learn intricate patterns.

## 3. Leveraging AI to Improve Business as a Store Owner

As a store owner, AI can be leveraged to significantly improve business operations and profitability by making data-driven decisions based on existing sales data.

Two examples of AI implementation are:

1.  **AI-Powered Demand Forecasting and Inventory Optimization:**

    *   **How it works:** AI models can analyze the store's historical sales data, taking into account factors like seasonality, promotions, holidays, and even external data like local events or weather patterns. These models learn complex relationships within the data to predict future demand for each product with high accuracy. For instance, a deep learning model could identify that sales of ice cream surge not just in summer but specifically on hot, sunny weekends when a local park hosts events.

    *   **Business Improvement:** By accurately forecasting demand, you can optimize your inventory levels. This means reducing instances of being out of stock for popular items (preventing lost sales) and minimizing excess inventory (reducing carrying costs, spoilage for perishable goods, and the need for markdowns). This leads to increased profitability and improved customer satisfaction because products are consistently available when customers want them.

2.  **AI-Driven Personalized Product Recommendations:**

    *   **How it works:** AI algorithms, particularly those used in recommendation systems, can analyze individual customer purchase history, browsing behavior (if you have an online store), and even demographic data to suggest products that a specific customer is likely to buy. For example, if a customer frequently buys coffee beans and milk, the AI might recommend a new coffee maker, a coffee grinder, or even complementary items like pastries or mugs that other coffee enthusiasts have purchased.

    *   **Business Improvement:** This personalized approach enhances the customer shopping experience, making it more relevant and efficient. It encourages customers to explore new products they might like, leading to increased average transaction value and repeat purchases. By understanding individual preferences, you can foster greater customer loyalty and create a more engaging retail environment. This also allows for more targeted marketing campaigns, as promotions can be tailored to specific customer segments identified by the AI.
