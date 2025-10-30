# Document Fraud Detection System

This project implements a document fraud detection system using Azure AI services, specifically designed for credit card document validation and analysis.

## Overview

The system provides a web interface built with Streamlit that allows users to upload documents (PDF, JPG, PNG) for fraud detection analysis. It utilizes Azure Document Intelligence and Blob Storage services to process and analyze credit card documents.

## Features

- Document upload interface
- Azure Blob Storage integration for document storage
- Credit card information extraction and validation
- Real-time document analysis feedback

## Architecture

The project is structured as follows:

```
Anti-fraud/
├── app.py              # Main application entry point
├── .env               # Environment variables configuration
└── src/
    ├── requirements.txt
    ├── services/
    │   ├── blob_service.py      # Azure Blob Storage integration
    │   └── credit_card_service.py # Credit card analysis service
    └── utilities/
        └── Config.py            # Configuration management
```

## Prerequisites

Required Python packages:

```python
azure.core
azure-ai-documentintelligence
streamlit
azure-storage-blob
python-dotenv
azure-ai-formrecognizer
```

## Configuration

Create a `.env` file in the root directory with the following variables:

```env
ENDPOINT=<your-azure-document-intelligence-endpoint>
SUBSCRIPTION_KEY=<your-azure-subscription-key>
AZURE_STORAGE_CONNECTION_STRING=<your-azure-storage-connection-string>
CONTAINER_NAME=<your-blob-container-name>
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Access the web interface through your browser

3. Upload a document containing credit card information

4. View the analysis results including:
   - Card holder name
   - Card number
   - Expiry date

## Components

### Web Interface ([`app.py`](app.py))
- Handles document upload
- Displays analysis results
- Provides user feedback

### Blob Service ([`blob_service.py`](src/services/blob_service.py))
- Manages document storage in Azure Blob Storage
- Handles file upload and URL generation

### Credit Card Service ([`credit_card_service.py`](src/services/credit_card_service.py))
- Integrates with Azure Document Intelligence
- Extracts and validates credit card information

### Configuration ([`Config.py`](src/utilities/Config.py))
- Manages environment variables
- Provides centralized configuration access

## Security Considerations

- Sensitive credentials are stored in `.env` file (not committed to version control)
- Azure Key Credential authentication is used for secure API access
- Document analysis is performed server-side

## Error Handling

The application includes error handling for:
- File upload failures
- Blob storage errors
- Document analysis failures
- Invalid credit card information