# Scheduling Questionnaires Setup and Support Guide

**Last Updated:** May 2, 2025

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 7F3E9A2D-5B8C-4E1F-9A6D-2C5F8B3E1A9D

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Questionnaire Design and Development](#questionnaire-design-and-development)
  - [Create Scheduling Questionnaires](#create-scheduling-questionnaires)
  - [Configure Question Types and Response Options](#configure-question-types-and-response-options)
  - [Implement Conditional Logic and Branching](#implement-conditional-logic-and-branching)
  - [Set Up Questionnaire Validation Rules](#set-up-questionnaire-validation-rules)
- [Integration with Scheduling Workflows](#integration-with-scheduling-workflows)
  - [Link Questionnaires to Visit Types](#link-questionnaires-to-visit-types)
  - [Configure Questionnaire Timing and Delivery](#configure-questionnaire-timing-and-delivery)
  - [Set Up Pre-Visit Questionnaire Requirements](#set-up-pre-visit-questionnaire-requirements)
- [Clinical Integration](#clinical-integration)
  - [Map Questionnaire Responses to Clinical Documentation](#map-questionnaire-responses-to-clinical-documentation)
  - [Configure Clinical Decision Support Integration](#configure-clinical-decision-support-integration)
  - [Set Up Provider Review Workflows](#set-up-provider-review-workflows)
- [Patient Experience and Communication](#patient-experience-and-communication)
  - [Customize Patient-Facing Questionnaire Interface](#customize-patient-facing-questionnaire-interface)
  - [Configure Reminder and Follow-Up Communications](#configure-reminder-and-follow-up-communications)
  - [Implement Accessibility and Multi-Language Support](#implement-accessibility-and-multi-language-support)

## Overview

Scheduling questionnaires enhance the appointment scheduling process by collecting important clinical and administrative information before the patient's visit. This pre-visit data collection improves clinical efficiency, enables better preparation for appointments, supports clinical decision-making, and enhances the overall patient care experience.

## Questionnaire Design and Development

### Create Scheduling Questionnaires

Design effective questionnaires that collect necessary information while maintaining patient engagement:

**Questionnaire Planning:**
1. **Purpose Definition**: Clearly define the clinical or administrative purpose
2. **Target Population**: Identify specific patient populations or visit types
3. **Information Requirements**: Determine essential vs. optional information
4. **Length Considerations**: Balance comprehensiveness with patient burden
5. **Integration Needs**: Plan for clinical documentation and workflow integration

**Design Principles:**
- Use clear, patient-friendly language
- Organize questions in logical sequence
- Minimize repetitive or redundant questions
- Include helpful explanations and context
- Consider patient literacy and health literacy levels

### Configure Question Types and Response Options

Utilize various question types to collect different types of information effectively:

**Question Type Options:**
1. **Multiple Choice**: Single or multiple selection options
2. **Text Entry**: Free text responses for detailed information
3. **Numeric Entry**: Numbers, measurements, dates, and quantities
4. **Rating Scales**: Likert scales and pain rating scales
5. **Yes/No Questions**: Binary responses for screening and eligibility
6. **Dropdown Lists**: Extensive option lists with search capability

**Response Configuration:**
- Required vs. optional question designation
- Default values and pre-populated responses
- Response validation rules and format requirements
- Conditional response options based on previous answers
- Clinical terminology integration (SNOMED, ICD-10)

### Implement Conditional Logic and Branching

Create dynamic questionnaires that adapt based on patient responses:

**Branching Logic Types:**
- Skip patterns that bypass irrelevant questions
- Show/hide logic for conditional question display
- Complex branching based on multiple response combinations
- Loop structures for repetitive information collection
- Exit conditions for early questionnaire completion

**Logic Configuration:**
1. Define trigger conditions and response criteria
2. Configure question dependencies and relationships
3. Set up validation rules for conditional responses
4. Test branching scenarios for all possible paths
5. Document logic flows for maintenance and updates

### Set Up Questionnaire Validation Rules

Implement validation to ensure data quality and completeness:

**Validation Types:**
- Required field validation and completion checking
- Format validation for dates, phone numbers, and emails
- Range validation for numeric responses
- Consistency checking across related questions
- Clinical logic validation for medical information

**Error Handling:**
- Clear error messages and correction guidance
- Progressive validation with real-time feedback
- Summary validation before questionnaire submission
- Integration with clinical decision support alerts
- Audit trails for validation failures and corrections

## Integration with Scheduling Workflows

### Link Questionnaires to Visit Types

Associate questionnaires with specific visit types and clinical scenarios:

**Visit Type Configuration:**
1. **Specialty-Specific Questionnaires**: Tailored for different medical specialties
2. **Procedure-Specific Questionnaires**: Pre-procedure screening and preparation
3. **New Patient Questionnaires**: Comprehensive intake for first-time patients
4. **Follow-Up Questionnaires**: Condition-specific monitoring and assessment
5. **Screening Questionnaires**: Preventive care and health maintenance

**Assignment Rules:**
- Automatic questionnaire assignment based on visit type
- Provider-specific questionnaire preferences
- Patient population-based questionnaire selection
- Override capabilities for special circumstances
- Multiple questionnaire assignments for complex visits

### Configure Questionnaire Timing and Delivery

Optimize when and how questionnaires are delivered to patients:

**Timing Options:**
- Immediate delivery upon appointment scheduling
- Scheduled delivery based on days before appointment
- Reminder-based delivery with escalation
- On-demand delivery for walk-in or same-day appointments
- Post-appointment questionnaires for follow-up

**Delivery Methods:**
1. **MyChart Integration**: Seamless questionnaire access through patient portal
2. **Email Delivery**: Direct email links with secure access
3. **SMS Text Messages**: Mobile-friendly questionnaire links
4. **Phone-Based Delivery**: Interactive voice response systems
5. **In-Office Completion**: Tablet or kiosk-based completion

### Set Up Pre-Visit Questionnaire Requirements

Establish requirements and policies for questionnaire completion:

**Completion Requirements:**
- Mandatory questionnaires for specific visit types
- Optional questionnaires with completion incentives
- Partial completion acceptance with follow-up
- Grace periods for questionnaire completion
- Alternative completion methods for non-compliant patients

**Workflow Integration:**
- Automatic appointment confirmation upon questionnaire completion
- Hold appointments pending questionnaire completion
- Provider notifications of questionnaire completion status
- Integration with check-in processes and registration
- Exception handling for urgent or emergent appointments

## Clinical Integration

### Map Questionnaire Responses to Clinical Documentation

Integrate questionnaire data with Epic's clinical documentation system:

**Documentation Mapping:**
1. **Flowsheet Integration**: Map responses to standard flowsheet rows
2. **Note Template Population**: Pre-populate clinical note templates
3. **Problem List Updates**: Automatically update problem lists
4. **Allergy Documentation**: Capture and document allergy information
5. **Medication Reconciliation**: Support medication history collection

**Data Integration:**
- Discrete data element mapping for analytics
- Free-text response integration with clinical notes
- Historical data tracking and trending
- Clinical decision support data integration
- Quality measure and registry data collection

### Configure Clinical Decision Support Integration

Leverage questionnaire data for clinical decision support and care improvement:

**Decision Support Applications:**
- Risk stratification based on questionnaire responses
- Clinical guideline compliance monitoring
- Preventive care recommendations and reminders
- Drug interaction and allergy checking
- Care gap identification and closure

**Alert Configuration:**
- Provider alerts for high-risk responses
- Automatic order suggestions based on responses
- Care coordination alerts for multidisciplinary teams
- Population health notifications for risk management
- Quality improvement alerts for best practice adherence

### Set Up Provider Review Workflows

Configure provider workflows for reviewing and acting on questionnaire responses:

**Review Process:**
1. **Pre-Visit Review**: Provider preparation and care planning
2. **Point-of-Care Review**: Real-time response review during visit
3. **Exception Review**: High-priority or concerning responses
4. **Care Coordination Review**: Team-based response evaluation
5. **Follow-Up Review**: Post-visit response analysis and planning

**Workflow Tools:**
- Dashboard views of questionnaire responses
- Integrated review within clinical documentation
- Prioritization of responses requiring attention
- Collaborative review tools for care teams
- Historical response trending and analysis

## Patient Experience and Communication

### Customize Patient-Facing Questionnaire Interface

Design user-friendly interfaces that encourage completion and engagement:

**Interface Design:**
- Branded questionnaire appearance matching organizational identity
- Mobile-responsive design for smartphone and tablet access
- Progress indicators and completion status
- Help text and explanatory information
- Skip and save functionality for partial completion

**Usability Features:**
1. **Intuitive Navigation**: Clear forward and backward navigation
2. **Auto-Save Functionality**: Automatic saving of responses
3. **Session Management**: Allow multiple sessions for completion
4. **Accessibility Features**: Screen reader compatibility and keyboard navigation
5. **Error Prevention**: Real-time validation and correction prompts

### Configure Reminder and Follow-Up Communications

Implement communication strategies to maximize questionnaire completion:

**Reminder Systems:**
- Automated email reminders with escalation
- SMS text message reminders for mobile engagement
- Phone call reminders for high-priority questionnaires
- MyChart message reminders with direct links
- Provider office staff manual follow-up protocols

**Communication Content:**
- Personalized reminder messages with patient name
- Clear instructions for questionnaire access and completion
- Benefits explanation for questionnaire completion
- Support contact information for technical assistance
- Deadline communication and urgency indicators

### Implement Accessibility and Multi-Language Support

Ensure questionnaires are accessible to all patient populations:

**Accessibility Features:**
- Section 508 compliance for disability access
- Screen reader compatibility and keyboard navigation
- High contrast and large font options
- Audio playback for questions and instructions
- Simple language options for low health literacy

**Multi-Language Support:**
1. **Translation Services**: Professional translation of questionnaire content
2. **Language Selection**: Patient choice of preferred language
3. **Cultural Adaptation**: Culturally appropriate question phrasing
4. **Interpreter Integration**: Connection with interpreter services
5. **Multilingual Support Staff**: Staff assistance for language barriers

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all scheduling questionnaire features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** 7F3E9A2D-5B8C-4E1F-9A6D-2C5F8B3E1A9D