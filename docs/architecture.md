# System Architecture Documentation

## Overview
This document outlines the architecture of the Medgemma Impact project.

## Components
- **Frontend**: Built with React, this component is responsible for the user interface.
- **Backend**: Developed using Node.js, it handles API requests and business logic.
- **Database**: MongoDB is used for data persistence.

## Architecture Diagram
```plaintext
+-------------+          +---------------+          +------------+  
|  Frontend   | <-----> |   Backend     | <-----> |  Database  |  
+-------------+          +---------------+          +------------+  
``` 

## Communication
- **Frontend** communicates with **Backend** via REST API.
- **Backend** communicates with **Database** using Mongoose.

## Conclusion
This document provides a high-level overview of the system architecture for the Medgemma Impact project. For more detailed information, refer to the respective component documentation.
