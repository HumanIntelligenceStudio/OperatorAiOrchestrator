# Referrals and Orders Setup and Support Guide

**Last Updated:** May 2, 2025

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 4C9A1F5B-8D2E-3B6F-7A4C-9E1D5F8B2A7C

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Referral Management System](#referral-management-system)
  - [Configure Referral Types and Categories](#configure-referral-types-and-categories)
  - [Set Up Provider Networks and Referral Routing](#set-up-provider-networks-and-referral-routing)
  - [Configure Authorization and Approval Workflows](#configure-authorization-and-approval-workflows)
  - [Implement Referral Tracking and Status Management](#implement-referral-tracking-and-status-management)
- [Order Management Integration](#order-management-integration)
  - [Link Orders with Referral Requests](#link-orders-with-referral-requests)
  - [Configure Order Sets for Common Referral Scenarios](#configure-order-sets-for-common-referral-scenarios)
  - [Set Up Clinical Decision Support for Referrals](#set-up-clinical-decision-support-for-referrals)
- [External Provider Integration](#external-provider-integration)
  - [Configure Care Everywhere for Referral Communication](#configure-care-everywhere-for-referral-communication)
  - [Set Up Electronic Referral Communication](#set-up-electronic-referral-communication)
  - [Manage External Provider Directory](#manage-external-provider-directory)
- [Quality and Compliance](#quality-and-compliance)
  - [Implement Referral Quality Metrics](#implement-referral-quality-metrics)
  - [Configure Compliance Monitoring](#configure-compliance-monitoring)
  - [Set Up Outcome Tracking](#set-up-outcome-tracking)

## Overview

The Referrals and Orders system in Epic manages the complex workflow of patient referrals from primary care to specialists, coordination of care between providers, and tracking of referral outcomes. This system integrates closely with scheduling, authorization management, and clinical documentation to provide comprehensive referral management.

## Referral Management System

### Configure Referral Types and Categories

Establish referral taxonomies that match your organization's clinical workflows:

**Referral Type Configuration:**
1. **Consultation Referrals**: Specialist opinion without ongoing care transfer
2. **Care Transfer Referrals**: Complete care responsibility transfer to specialist
3. **Procedure Referrals**: Specific procedures or interventions
4. **Diagnostic Referrals**: Imaging, testing, or diagnostic evaluations
5. **Therapy Referrals**: Physical therapy, occupational therapy, counseling

**Category Setup Elements:**
- Clinical specialty and subspecialty categorization
- Urgency levels (routine, urgent, emergent, STAT)
- Authorization requirements and approval workflows
- Documentation requirements and clinical information needs
- Insurance and payer-specific routing rules

### Set Up Provider Networks and Referral Routing

Configure provider networks to support efficient referral routing:

**Network Configuration:**
- Internal provider networks within the organization
- External provider networks and community partners
- Specialty-specific networks and subspecialty providers
- Geographic networks for location-based routing
- Insurance network participation and contracted providers

**Routing Logic:**
1. **Provider Preference Routing**: Based on referring provider preferences
2. **Patient Choice Routing**: Allow patients to select from qualified providers
3. **Geographic Routing**: Route based on patient location and convenience
4. **Network Routing**: Route based on insurance participation
5. **Capacity-Based Routing**: Consider provider availability and capacity

### Configure Authorization and Approval Workflows

Implement authorization processes to ensure appropriate care and cost management:

**Authorization Types:**
- Insurance prior authorization requirements
- Internal utilization management reviews
- Specialty-specific clinical criteria
- High-cost procedure approvals
- Out-of-network referral approvals

**Workflow Configuration:**
1. Automated authorization checking based on referral type
2. Clinical decision support integration for appropriateness
3. Workflow routing to utilization management staff
4. Provider notification of authorization status
5. Patient communication about authorization requirements

### Implement Referral Tracking and Status Management

Monitor referral progress and outcomes throughout the care continuum:

**Status Tracking Elements:**
- Referral creation and initial routing
- Authorization status and approval tracking
- Appointment scheduling and confirmation
- Care delivery and procedure completion
- Follow-up communication and care coordination
- Outcome documentation and quality metrics

**Communication Framework:**
- Automated status updates to referring providers
- Patient notifications about referral progress
- Specialty provider acknowledgment and feedback
- Care coordination team notifications
- Quality team outcome reporting

## Order Management Integration

### Link Orders with Referral Requests

Integrate referral management with clinical order processing:

**Integration Points:**
1. **Diagnostic Orders**: Link imaging and lab orders with referrals
2. **Procedure Orders**: Connect procedure referrals with scheduling
3. **Medication Orders**: Coordinate specialty medication management
4. **Therapy Orders**: Link referrals with therapy scheduling and tracking
5. **Follow-up Orders**: Ensure appropriate post-referral care coordination

**Workflow Benefits:**
- Reduced duplicate data entry
- Improved care coordination and communication
- Enhanced tracking of referral outcomes
- Better quality reporting and metrics
- Streamlined provider workflows

### Configure Order Sets for Common Referral Scenarios

Standardize referral processes with predefined order sets:

**Order Set Categories:**
- Specialty-specific referral order sets
- Condition-based referral protocols
- Screening and prevention referral sets
- Emergency and urgent referral protocols
- Post-discharge referral coordination sets

**Order Set Components:**
- Standardized referral documentation templates
- Required diagnostic tests and preparation
- Patient education materials and instructions
- Follow-up scheduling and care coordination
- Quality metrics and outcome tracking

### Set Up Clinical Decision Support for Referrals

Implement evidence-based decision support for appropriate referrals:

**Decision Support Types:**
1. **Appropriateness Criteria**: Evidence-based referral guidelines
2. **Alternative Treatment Suggestions**: Non-referral treatment options
3. **Provider Recommendations**: Best-match provider suggestions
4. **Cost Information**: Treatment cost and insurance coverage data
5. **Quality Metrics**: Provider performance and outcome data

**Implementation Strategy:**
- Integrate clinical guidelines and best practices
- Provide real-time decision support during referral creation
- Offer educational resources and clinical evidence
- Track adherence to recommended guidelines
- Monitor outcomes and quality improvements

## External Provider Integration

### Configure Care Everywhere for Referral Communication

Enable seamless communication with external providers:

**Care Everywhere Setup:**
- Configure organization connectivity and trust relationships
- Set up patient matching and identity management
- Enable clinical data sharing and document exchange
- Configure referral-specific communication templates
- Implement security and privacy controls

**Communication Features:**
- Automated referral notifications to external providers
- Clinical summary sharing with referral requests
- Real-time status updates and acknowledgments
- Outcome reporting and care coordination feedback
- Patient portal integration for external referrals

### Set Up Electronic Referral Communication

Implement electronic referral networks and communication standards:

**Electronic Referral Systems:**
- HL7 FHIR-based referral messaging
- Direct Trust messaging for secure communication
- State and regional health information exchanges
- Specialty-specific referral networks
- Telemedicine platform integration

**Communication Standards:**
- Standardized referral message formats
- Clinical data sharing requirements
- Patient consent and authorization management
- Security and encryption protocols
- Audit trails and compliance monitoring

### Manage External Provider Directory

Maintain comprehensive directory of referral providers:

**Provider Directory Elements:**
- Provider demographics and contact information
- Specialty and subspecialty capabilities
- Hospital affiliations and practice locations
- Insurance participation and network status
- Quality metrics and patient satisfaction scores
- Referral preferences and communication methods

**Directory Maintenance:**
- Regular updates from credentialing systems
- Provider self-service update capabilities
- Integration with state licensing databases
- Quality monitoring and performance tracking
- Patient feedback and outcome integration

## Quality and Compliance

### Implement Referral Quality Metrics

Track and monitor referral effectiveness and quality:

**Quality Metrics:**
1. **Access Metrics**: Time from referral to appointment
2. **Appropriateness Metrics**: Evidence-based referral compliance
3. **Outcome Metrics**: Clinical outcomes and patient satisfaction
4. **Communication Metrics**: Provider and patient communication effectiveness
5. **Cost Metrics**: Referral costs and resource utilization

**Reporting and Analytics:**
- Dashboard reporting for referral patterns and trends
- Provider-specific performance metrics
- Patient population analysis and outcomes
- Specialty service line performance
- Network adequacy and access analysis

### Configure Compliance Monitoring

Ensure referral processes meet regulatory and organizational requirements:

**Compliance Areas:**
- Insurance authorization and prior approval requirements
- Clinical documentation and medical necessity
- Patient consent and privacy protections
- Network adequacy and access standards
- Quality reporting and outcome measurement

**Monitoring Systems:**
- Automated compliance checking and alerts
- Regular audit processes and documentation
- Exception reporting and corrective actions
- Training and education for compliance updates
- Continuous improvement and policy updates

### Set Up Outcome Tracking

Monitor referral outcomes to improve quality and effectiveness:

**Outcome Tracking Elements:**
- Clinical outcomes and patient improvement
- Patient satisfaction with referral experience
- Provider satisfaction with referral process
- Cost-effectiveness and resource utilization
- Care coordination and communication quality

**Improvement Processes:**
- Regular outcome review and analysis
- Provider feedback and quality improvement
- Patient feedback integration and response
- Best practice identification and sharing
- Continuous process improvement and optimization

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all referral and order management features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** 4C9A1F5B-8D2E-3B6F-7A4C-9E1D5F8B2A7C