# Interpreter Scheduling Setup and Support Guide

**Last Updated:** November 1, 2024

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** C7CE8334-1D15-4A95-B54F-A96C8E73D72F

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Available Epic Resources](#available-epic-resources)
- [Interpreter Scheduling: Strategy](#interpreter-scheduling-strategy)
  - [Decide Whether Epic's Interpreter Scheduling Is a Good Fit for Your Organization](#decide-whether-epics-interpreter-scheduling-is-a-good-fit-for-your-organization)
  - [Evaluate Your Organization's Interpreter Needs](#evaluate-your-organizations-interpreter-needs)
  - [Decide How to Schedule Interpreters](#decide-how-to-schedule-interpreters)
  - [Decide How to Handle Interpreters for Minor Patients](#decide-how-to-handle-interpreters-for-minor-patients)
- [Interpreter Scheduling Setup: Essentials](#interpreter-scheduling-setup-essentials)
  - [Enable Interpreter Scheduling in Your System](#enable-interpreter-scheduling-in-your-system)

## Overview

Epic's interpreter scheduling functionality helps your organization coordinate language interpretation services for patients who need them. This system allows you to schedule interpreters alongside patient appointments, ensuring that language barriers don't prevent patients from receiving quality healthcare.

The interpreter scheduling system integrates with Epic's appointment scheduling functionality to provide seamless coordination of interpretation services, whether using staff interpreters, contracted interpreters, or video remote interpretation services.

## Available Epic Resources

Epic provides several resources to help you implement interpreter scheduling:

- Foundation System examples and configurations
- Best practice documentation for interpreter coordination
- Integration guides for third-party interpretation services
- Training materials for scheduling staff

## Interpreter Scheduling: Strategy

Before implementing interpreter scheduling, consider your organization's specific needs and how Epic's interpreter scheduling functionality can best serve your patient population.

### Decide Whether Epic's Interpreter Scheduling Is a Good Fit for Your Organization

Epic's interpreter scheduling is most beneficial for organizations that:

- Have a significant patient population requiring interpretation services
- Use staff interpreters or contracted interpretation services
- Need to coordinate interpreter schedules with patient appointments
- Want to track interpreter utilization and costs
- Need reporting on interpretation services provided

Consider whether your current interpretation coordination methods are meeting your needs or if Epic's integrated approach would provide better service coordination and documentation.

### Evaluate Your Organization's Interpreter Needs

Assess your organization's interpreter requirements:

1. **Languages Needed**: Identify the most common languages requiring interpretation at your organization
2. **Service Delivery Methods**: Determine if you use in-person interpreters, video remote interpretation, telephone interpretation, or a combination
3. **Interpreter Resources**: Catalog your available interpreter resources (staff, contracted, agency)
4. **Scheduling Patterns**: Understand when and where interpretation services are most needed
5. **Compliance Requirements**: Consider any regulatory requirements for interpretation services in your area

### Decide How to Schedule Interpreters

Epic supports several approaches to interpreter scheduling:

- **Direct Scheduling**: Schedule interpreters directly for specific appointments
- **Pool-Based Scheduling**: Use interpreter pools to allow flexible assignment
- **Automatic Requests**: Set up automatic interpreter requests based on patient language preferences
- **Third-Party Integration**: Integrate with external interpretation service providers

Choose the approach that best fits your organization's workflow and interpreter resource model.

### Decide How to Handle Interpreters for Minor Patients

Consider special requirements for pediatric patients:

- Parent/guardian language preferences may differ from patient preferences
- Special consideration for adolescent patients who may prefer different interpretation arrangements
- Compliance with local regulations regarding interpretation for minors

## Interpreter Scheduling Setup: Essentials

### Enable Interpreter Scheduling in Your System

Basic system configuration steps:

1. **Enable Interpreter Functionality**: Turn on interpreter scheduling features in system definitions
2. **Configure Language Records**: Set up language master file records for languages requiring interpretation
3. **Set Up Interpreter Resources**: Create interpreter records in the provider/resource master file
4. **Configure Interpreter Types**: Define different types of interpretation services (staff, contracted, video, etc.)
5. **Set Up Scheduling Rules**: Define rules for automatic interpreter requests and scheduling

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all interpreter scheduling features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** C7CE8334-1D15-4A95-B54F-A96C8E73D72F