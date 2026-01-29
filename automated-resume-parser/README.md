# Automated Resume Parser & Job Matcher

## Project Overview

An intelligent recruitment tool that leverages **AWS AI Services** to automate the extraction of data from resumes and match candidates to suitable job descriptions. This serverless application eliminates manual data entry and streamlines the hiring process.

## Architecture

- **Frontend**: React.js for the user interface (Resume Upload & Results Dashboard).
- **Backend**: Python-based AWS Lambda functions.
- **AI/ML Engine**:
  - **AWS Textract**: To extract raw text and structured data from PDF resumes.
  - **OpenAI API / AWS Bedrock**: To analyze context, summarize profiles, and score relevance against job descriptions.
- **Storage**:
  - **Amazon S3**: Secure storage for uploaded resume documents.
  - **Amazon DynamoDB**: NoSQL database for storing parsed metadata and user profiles.
- **API**: AWS API Gateway for RESTful communication.

## Key Features

- **Drag-and-Drop Upload**: Seamless UI for uploading PDF/DOCX resumes.
- **Automated Parsing**: Instantly extracts Name, Email, Skills, Experience, and Education using OCR and NLP.
- **Smart Matching Logic**: compare candidate profiles against job requirements and generate a "Fit Score".
- **Searchable Database**: fast retrieval of candidates based on specific skills or keywords.

## Technologies Used

- **Cloud**: AWS (Lambda, S3, DynamoDB, API Gateway, Textract)
- **Frontend**: React.js, Tailwind CSS
- **Language**: Python, JavaScript
- **Infrastructure as Code**: Terraform / SAM
