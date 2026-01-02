# stock-market-realtime-data-pipeline
An end-to-end real-time data engineering project that simulates live stock market data, streams it through Apache Kafka, stores it in an AWS data lake, and enables serverless analytics using Amazon Athena.

This project is designed to demonstrate real-world streaming architecture, cloud-native data engineering, and production-aligned best practices.

Architecture -- 
Stock Market Simulator (Python)
        |
        v
Kafka Producer  --->  Apache Kafka (EC2)
                          |
                          v
                    Kafka Consumer
                          |
                          v
                      Amazon S3
                          |
               AWS Glue Crawler & Catalog
                          |
                          v
                    Amazon Athena

🔧 Tech Stack

Language: Python 3.10

Streaming: Apache Kafka

Cloud: AWS

EC2 (Kafka hosting)

S3 (Data Lake)

Glue Crawler & Data Catalog

Athena (SQL analytics)

SDK: Boto3

Data Format: JSON / Parquet

Containerization: Docker (Kafka & Zookeeper)
