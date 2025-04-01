# AI-Powered Local Tourism Recommender

## Overview

This project aims to provide personalized travel recommendations by segmenting tourism data in India based on geographic location, significance of places, and Google reviews. It uses clustering techniques to uncover patterns influencing tourist preferences and behaviors.

## Problem Statement

Tourists need personalized travel recommendations that adapt to individual preferences, popularity trends, and customer sentiments.

## Approach

Pairwise clustering using DBSCAN, K-Means, and Hierarchical Clustering to segment data in three key areas:

*   **Geographic Clustering**: Identifies tourist hotspots.
*   **Significance-Based Clustering**: Understands visit patterns based on place type, fee, and duration.
*   **Review-Based Clustering**: Analyzes how ratings, review counts, and fees impact customer experiences.

## Data Source

*   **Travel Dataset: Guide to India's Must See Places (Kaggle)**: [https://www.kaggle.com/datasets/saketk511/travel-dataset-guide-to-indias-must-see-places](https://www.kaggle.com/datasets/saketk511/travel-dataset-guide-to-indias-must-see-places)

## Key Steps

1.  **Data Preprocessing**: Handling missing values, duplicate removal, feature selection, encoding (Label Encoding), and scaling (Standard Scaler).
2.  **Clustering**: Applying K-Means, Hierarchical Clustering, and DBSCAN.

## Results

*   Identified popular regions, high-rated cities, fee structures for different site types, and correlation between visit duration and reviews.

## Conclusion

The project provides insights for improving customer targeting, optimizing pricing, enhancing marketing, and personalizing recommendations.

## Authors

*   Vishal Dangiwala
*   Deepali Malik

