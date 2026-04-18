🌍 Air Quality Index (AQI) Analysis & Prediction

📌 Overview

This project presents a data-driven analysis of Air Quality Index (AQI) using real-world environmental data. It focuses on understanding pollution patterns and building a predictive model using machine learning techniques.

The dataset is sourced from the Government of India open data platform (data.gov.in).

📊 Dataset

  Source:   https://www.data.gov.in/resource/real-time-air-quality-index-various-locations

  Features:

   &#x20; - pollutant\_min  

   &#x20; - pollutant\_max  

   &#x20; - pollutant\_avg  

   The dataset represents pollution levels across different states and cities, enabling regional analysis of air quality.

⚙️ Methodology

🔹Data Preprocessing

  Missing value handling (mean imputation)

  Outlier detection and removal using IQR

  Feature scaling using Min-Max normalization

🔹Exploratory Data Analysis

  State-wise and city-wise pollution comparison  

  Distribution analysis (histograms)  

  Correlation analysis (heatmaps)  

  Feature relationship analysis (scatter plots)  

🔹Model Development

  Model: Linear Regression  

  Input Features: pollutant\_min, pollutant\_max  

  Target Variable: pollutant\_avg  

📈 Results

  | Metric | Value |

  |-------|------|

  | R² Score | 0.9271 |

  | MAE | 4.54 |

  | MSE | 57.97 |

  The model demonstrates strong predictive performance with high accuracy and low error values.

📸 Visualizations

🔹Top Polluted States

![Top States](https://github.com/kumaradi9508/AQI-Analysis-and-Prediction/blob/07aedac1d01a8db1ecdba92e7ec8ef0c90049026/images/fig1.png)


🔹Distribution of Pollution Levels

![Distribution Analysis](https://github.com/kumaradi9508/AQI-Analysis-and-Prediction/blob/07aedac1d01a8db1ecdba92e7ec8ef0c90049026/images/fig3.png)

🔹Correlation Heatmap

![Heatmap](https://github.com/kumaradi9508/AQI-Analysis-and-Prediction/blob/07aedac1d01a8db1ecdba92e7ec8ef0c90049026/images/fig5.png)

🔹Actual vs Predicted

![Prediction](https://github.com/kumaradi9508/AQI-Analysis-and-Prediction/blob/07aedac1d01a8db1ecdba92e7ec8ef0c90049026/images/fig10.png)

🛠 Tech Stack

   Python  

   Pandas  

   NumPy  

   Matplotlib  

   Seaborn  

   Scikit-learn  

⚠️ Limitations

   Absence of temporal (time-series) data  

   Lack of meteorological features (temperature, humidity, wind speed)  

   Limited feature set  

🚀 Future Work

   Implementation of advanced models (e.g., XGBoost)  

   Integration of weather data  

   Time-series forecasting  

📄 Documentation

  The complete IEEE-format report is available here:  

  👉 [View Report](https://github.com/kumaradi9508/AQI-Analysis-and-Prediction/blob/07aedac1d01a8db1ecdba92e7ec8ef0c90049026/report/AQI_Report.pdf)

👨‍💻 Author

Aditya Kumar  

B.Tech Computer Science Engineering  

Lovely Professional University  

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

