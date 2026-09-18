# Internal Service Agent

AI-powered internal IT Service Desk Agent that helps employees resolve common IT issues, find approved internal procedures, ask for clarification, and escalate risky or unsupported requests.

## Project Overview

The Internal Service Agent is designed to act as a first-level IT Service Desk assistant.

The agent:

- Understands employee IT requests
- Categorizes issues automatically
- Searches the internal knowledge base
- Provides approved troubleshooting guidance
- Detects security-sensitive requests
- Escalates risky or unclear issues
- Creates structured IT support tickets
- Maintains an audit trail
- Shows the knowledge-base source used for the response

## Key Features

### 1. Issue Understanding
The agent analyzes an employee's message and identifies the type of IT issue.

Supported categories include:

- VPN
- Password
- Network
- Email
- Printer
- Hardware
- Software
- Access
- General IT issues

### 2. Knowledge Base Search

The agent searches the internal IT knowledge base for approved procedures.

The knowledge base includes policies for:

- Password Reset
- VPN Access
- Laptop Replacement
- Software Installation
- Printer Troubleshooting
- Email Mailbox Quota
- Guest Wi-Fi
- Expense Software Access
- Security Incident Reporting
- Work-From-Home Equipment

### 3. Security & Escalation

Security-sensitive requests are automatically escalated.

Examples include:

- Suspected hacking
- Compromised accounts
- Phishing
- Malware
- Ransomware
- Requests to bypass security
- Requests involving administrator passwords
- Requests to disable MFA

High-risk requests receive a high-priority support ticket.

### 4. Ticketing

When an issue cannot be safely resolved using the approved knowledge base, the agent creates a structured support ticket containing:

- Ticket ID
- Category
- Employee issue
- Priority
- Escalation reason

### 5. Audit Trail

Important agent actions are recorded in the audit log, including:

- Employee request
- Issue category
- Action performed
- Result
- Knowledge-base source
- Ticket ID when applicable

## System Architecture

```text
Employee Request
       |
       v
   Agent Layer
       |
       v
Issue Categorization
       |
       +-------------------+
       |                   |
       v                   v
 Risk Detection      Knowledge Base
       |                   |
       v                   v
 Escalation          Approved Guidance
       |                   |
       v                   v
    Ticket             Response
       |
       v
   Audit Log

