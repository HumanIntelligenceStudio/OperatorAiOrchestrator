# Sign In, Check In, and Check Out Setup and Support Guide

**Last Updated:** May 2, 2025

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 9B5E8A1D-3F7C-4E2A-8B6F-1D9E5A3C7F2B

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Patient Arrival and Sign-In](#patient-arrival-and-sign-in)
  - [Configure Self-Service Check-In Kiosks](#configure-self-service-check-in-kiosks)
  - [Set Up Mobile Check-In Through MyChart](#set-up-mobile-check-in-through-mychart)
  - [Configure Traditional Front Desk Check-In](#configure-traditional-front-desk-check-in)
  - [Implement Patient Identity Verification](#implement-patient-identity-verification)
- [Check-In Process Workflows](#check-in-process-workflows)
  - [Configure Department-Specific Check-In Requirements](#configure-department-specific-check-in-requirements)
  - [Set Up Insurance Verification and Eligibility Checking](#set-up-insurance-verification-and-eligibility-checking)
  - [Configure Copay Collection and Financial Processes](#configure-copay-collection-and-financial-processes)
  - [Implement Pre-Visit Questionnaire Integration](#implement-pre-visit-questionnaire-integration)
- [Visit Management and Flow](#visit-management-and-flow)
  - [Configure Patient Flow and Room Assignment](#configure-patient-flow-and-room-assignment)
  - [Set Up Provider and Staff Notifications](#set-up-provider-and-staff-notifications)
  - [Implement Wait Time Management](#implement-wait-time-management)
- [Check-Out and Post-Visit Processes](#check-out-and-post-visit-processes)
  - [Configure Automated Check-Out Workflows](#configure-automated-check-out-workflows)
  - [Set Up Follow-Up Appointment Scheduling](#set-up-follow-up-appointment-scheduling)
  - [Implement Post-Visit Instructions and Communication](#implement-post-visit-instructions-and-communication)

## Overview

The Sign In, Check In, and Check Out processes are critical touchpoints in the patient experience that directly impact operational efficiency, patient satisfaction, and clinical workflow. Epic provides multiple options for managing these processes, from traditional front desk interactions to modern self-service technologies that empower patients while reducing administrative burden.

## Patient Arrival and Sign-In

### Configure Self-Service Check-In Kiosks

Deploy patient-operated kiosks to streamline the arrival process:

**Kiosk Configuration Options:**
1. **Hardware Setup**: Touch screen kiosks with integrated peripherals
2. **Software Configuration**: Epic-integrated check-in applications
3. **Identity Verification**: ID scanning, photo capture, signature collection
4. **Insurance Processing**: Card scanning and eligibility verification
5. **Form Completion**: Digital completion of required forms and updates

**Kiosk Placement Strategy:**
- High-traffic entrance areas for maximum visibility
- Multiple kiosks for high-volume departments
- ADA-compliant placement and accessibility features
- Staff supervision stations for assistance
- Integration with queue management systems

### Set Up Mobile Check-In Through MyChart

Enable patients to check in using their personal mobile devices:

**Mobile Check-In Features:**
- GPS-based arrival detection and automatic prompts
- QR code scanning for appointment identification
- Digital form completion and signature capture
- Insurance card photo upload and verification
- Real-time communication with clinical staff

**Configuration Elements:**
1. **Arrival Detection Settings**: Geographic radius and timing parameters
2. **Security Configuration**: Multi-factor authentication and identity verification
3. **Form Integration**: Pre-visit questionnaires and required documentation
4. **Notification Setup**: Patient and staff notification preferences
5. **Exception Handling**: Processes for check-in failures or issues

### Configure Traditional Front Desk Check-In

Optimize staff-assisted check-in processes for efficiency and accuracy:

**Front Desk Workflow Configuration:**
- Streamlined check-in screens with essential information
- Integration with scheduling systems and appointment details
- Automated insurance eligibility checking and verification
- Copay calculation and collection integration
- Exception handling for special circumstances

**Staff Efficiency Tools:**
- Patient search and identification tools
- Quick access to frequently needed functions
- Integration with communication systems
- Quality control checkpoints and validation
- Training resources and procedural guidance

### Implement Patient Identity Verification

Ensure accurate patient identification and reduce medical errors:

**Verification Methods:**
1. **Photo ID Verification**: Driver's license or state ID checking
2. **Biometric Verification**: Fingerprint or facial recognition systems
3. **Two-Factor Authentication**: Multiple identifier confirmation
4. **Insurance Card Verification**: Real-time eligibility and benefits checking
5. **Previous Visit Verification**: Historical information confirmation

**Security and Privacy:**
- HIPAA-compliant identity verification processes
- Secure storage and handling of identity documents
- Audit trails for identity verification activities
- Privacy protection for sensitive patient information
- Integration with organizational security policies

## Check-In Process Workflows

### Configure Department-Specific Check-In Requirements

Customize check-in processes for different clinical departments:

**Department Customization:**
- Specialty-specific forms and questionnaires
- Unique workflow requirements and procedures
- Integration with department-specific systems
- Staff role configuration and permissions
- Performance metrics and quality measures

**Common Department Configurations:**
1. **Primary Care**: Comprehensive health maintenance and preventive care forms
2. **Specialty Care**: Condition-specific questionnaires and preparation requirements
3. **Surgical Services**: Pre-operative assessment and consent processes
4. **Emergency Department**: Rapid triage and acuity assessment integration
5. **Diagnostic Services**: Procedure preparation and safety screening

### Set Up Insurance Verification and Eligibility Checking

Automate insurance verification to reduce claim denials and improve revenue:

**Verification Components:**
- Real-time eligibility checking with insurance carriers
- Benefits verification and coverage determination
- Prior authorization requirement identification
- Copay and deductible calculation
- Network participation verification

**Integration Features:**
1. **Automatic Verification**: Scheduled batch processing and real-time checking
2. **Exception Handling**: Manual verification for special circumstances
3. **Alert Systems**: Staff notifications for verification issues
4. **Documentation**: Verification results storage and audit trails
5. **Reporting**: Verification success rates and issue tracking

### Configure Copay Collection and Financial Processes

Optimize financial processes to improve cash flow and reduce bad debt:

**Financial Process Configuration:**
- Automated copay calculation based on insurance benefits
- Multiple payment method acceptance (cash, card, mobile payments)
- Payment plan setup and management
- Financial assistance program integration
- Collection policy enforcement and documentation

**Payment Processing Integration:**
- Point-of-service payment collection
- Integration with billing systems and accounts receivable
- Real-time insurance eligibility and benefit verification
- Automated receipt generation and documentation
- Financial counselor referral processes

### Implement Pre-Visit Questionnaire Integration

Connect pre-visit questionnaires with check-in processes:

**Questionnaire Integration:**
1. **Completion Verification**: Check questionnaire completion status
2. **Review and Updates**: Allow patients to review and modify responses
3. **Clinical Alert Generation**: Flag concerning responses for provider attention
4. **Documentation Integration**: Automatically populate clinical documentation
5. **Follow-Up Requirements**: Identify additional forms or processes needed

**Workflow Benefits:**
- Reduced visit time through pre-visit data collection
- Improved clinical preparation and care planning
- Enhanced patient engagement and communication
- Better clinical documentation and quality metrics
- Streamlined provider workflows and efficiency

## Visit Management and Flow

### Configure Patient Flow and Room Assignment

Optimize patient movement through clinical areas:

**Flow Management Components:**
- Real-time tracking of patient location and status
- Automated room assignment based on availability and requirements
- Integration with clinical staff schedules and availability
- Queue management and wait time optimization
- Bottleneck identification and resolution

**Room Assignment Logic:**
1. **Automatic Assignment**: Based on appointment type and room requirements
2. **Manual Override**: Staff ability to make assignment changes
3. **Preference Integration**: Patient and provider room preferences
4. **Equipment Requirements**: Specialized equipment and resource availability
5. **Efficiency Optimization**: Minimize walking distance and wait times

### Set Up Provider and Staff Notifications

Configure communication systems to keep care teams informed:

**Notification Types:**
- Patient arrival and check-in confirmation
- Room assignment and readiness alerts
- Urgent or priority patient notifications
- Schedule changes and appointment updates
- Clinical alerts and safety notifications

**Communication Methods:**
1. **Electronic Notifications**: Epic in-basket messages and alerts
2. **Mobile Notifications**: Smartphone and tablet push notifications
3. **Desktop Alerts**: Pop-up notifications and status indicators
4. **Physical Systems**: Paging systems and overhead announcements
5. **Integration Systems**: Nurse call systems and communication boards

### Implement Wait Time Management

Monitor and optimize patient wait times throughout the visit:

**Wait Time Tracking:**
- Real-time monitoring of wait times at each process step
- Historical analysis and trending of wait time patterns
- Identification of bottlenecks and process inefficiencies
- Patient communication about expected wait times
- Staff productivity and efficiency metrics

**Optimization Strategies:**
- Dynamic scheduling adjustments based on real-time flow
- Staff reallocation to address bottlenecks
- Patient communication and expectation management
- Process improvement initiatives based on data analysis
- Integration with patient satisfaction surveys and feedback

## Check-Out and Post-Visit Processes

### Configure Automated Check-Out Workflows

Streamline the visit conclusion process:

**Automated Check-Out Features:**
1. **Appointment Completion**: Automatic status updates and documentation
2. **Billing Integration**: Charge capture and claim submission
3. **Follow-Up Scheduling**: Automatic appointment scheduling based on provider orders
4. **Prescription Processing**: Electronic prescription transmission
5. **Patient Communication**: Automated instructions and follow-up information

**Workflow Automation:**
- Integration with clinical documentation systems
- Automatic generation of visit summaries and instructions
- Insurance claim preparation and submission
- Quality measure documentation and reporting
- Patient portal message generation and delivery

### Set Up Follow-Up Appointment Scheduling

Ensure continuity of care through efficient follow-up scheduling:

**Follow-Up Configuration:**
- Provider order integration for recommended follow-up
- Automatic scheduling based on clinical protocols
- Patient preference integration and scheduling flexibility
- Multiple appointment coordination for complex patients
- Insurance authorization management for follow-up services

**Scheduling Optimization:**
1. **Protocol-Based Scheduling**: Evidence-based follow-up timing
2. **Patient Convenience**: Flexible scheduling options and preferences
3. **Provider Availability**: Integration with provider schedules and capacity
4. **Resource Coordination**: Multi-appointment and resource scheduling
5. **Communication Integration**: Appointment confirmation and reminders

### Implement Post-Visit Instructions and Communication

Provide patients with comprehensive post-visit information and support:

**Instruction Delivery Methods:**
- Printed instructions and educational materials
- Electronic delivery through patient portals
- SMS text message summaries and reminders
- Email communication with detailed instructions
- Mobile app integration for ongoing engagement

**Communication Content:**
1. **Visit Summary**: Key findings, diagnoses, and treatment plans
2. **Medication Instructions**: Prescription information and administration guidance
3. **Follow-Up Requirements**: Appointment scheduling and care coordination
4. **Educational Resources**: Condition-specific information and resources
5. **Contact Information**: Provider contact details and emergency instructions

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all sign-in, check-in, and check-out features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** 9B5E8A1D-3F7C-4E2A-8B6F-1D9E5A3C7F2B