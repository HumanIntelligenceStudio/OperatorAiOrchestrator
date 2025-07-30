# Book Anywhere Setup and Support Guide

**Last Updated:** October 8, 2024

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 3397E6D0-A189-492C-AEA3-4218FDC75A06

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Book Anywhere Outgoing/Client Setup](#book-anywhere-outgoingclient-setup)
  - [Join the Book Anywhere Network](#join-the-book-anywhere-network)
  - [Create Records to Represent Scheduling Locations](#create-records-to-represent-scheduling-locations)
  - [Allow Visit Types to Be Scheduled Externally](#allow-visit-types-to-be-scheduled-externally)
  - [Specify Default Indications for Book Anywhere Visit Types](#specify-default-indications-for-book-anywhere-visit-types)
  - [Specify Default Places of Service for Book Anywhere Scheduling](#specify-default-places-of-service-for-book-anywhere-scheduling)
  - [Create Reasons Why Appointments Are Scheduled Externally](#create-reasons-why-appointments-are-scheduled-externally)
  - [Give Users Security to Schedule Book Anywhere Appointments](#give-users-security-to-schedule-book-anywhere-appointments)
  - [Customize Scheduling Preference Time Ranges for Book Anywhere](#customize-scheduling-preference-time-ranges-for-book-anywhere)
- [Book Anywhere Incoming/Server Setup](#book-anywhere-incomingserver-setup)
  - [Join the Book Anywhere Network](#join-the-book-anywhere-network-1)
  - [Create a Background User for Scheduling Book Anywhere Appointments](#create-a-background-user-for-scheduling-book-anywhere-appointments)
  - [Allow Book Anywhere to Create Potential Duplicate Patients](#allow-book-anywhere-to-create-potential-duplicate-patients)
  - [Allow Book Anywhere to Create Verified Patients](#allow-book-anywhere-to-create-verified-patients)
  - [Create Your Book Anywhere Decision Tree](#create-your-book-anywhere-decision-tree)
  - [Test Your Book Anywhere Decision Tree](#test-your-book-anywhere-decision-tree)
  - [Show Schedulers Which Organization Scheduled an Appointment](#show-schedulers-which-organization-scheduled-an-appointment)

## Overview

Use Book Anywhere to help patients get the care they need by allowing schedulers to directly schedule appointments at other Epic organizations.

- Health systems and retail clinics can partner to use Book Anywhere.
  - Retail clinics can schedule appointments at a local health system for patients who need more specialized care than the retail clinic can provide.
  - Health systems with full schedules can schedule appointments for patients to receive routine care at retail clinics.
- Share resources with partner organizations by using Book Anywhere to schedule remote video visits.

Book Anywhere uses FHIR to search for available appointment slots at another organization, find or create a patient record at that organization, and then schedule that patient into a slot. Book Anywhere also uses Care Everywhere to match, link, and create patients across organizations. Care Everywhere is used starting in November 2022 and in the following versions with special updates:

- May 2022: E10200037, C10200037-HSWeb, E10203746, E10203747, E10204333, E10208697
- February 2022: E10105718, C10105718-HSWeb, E10109526, E10109556, E10109998, E10113275
- November 2021: E9909840, C9909840-HSWeb, E9913017, E9913035, E991333

Note: The specified special updates for November 2021 require that your organization is using Care Everywhere in order to work.

## How It Works

Patient Greg just saw his PCP at the Four Lakes Family Clinic and needs to follow up with an endocrinologist for his diabetes. The Four Lakes scheduler searches for appointments at local organizations that have agreed to take endocrinology patients. Greg leaves with his follow up appointment scheduled for him.

From a patient's Appointment Desk, schedulers click Book It to schedule appointments using Book Anywhere. On the left side of the activity, they select the visit type they want to schedule and they enter the locations to search. They can also enter the patient's indications and a specialty for the visit. Including this information in the search helps the external organization send back appropriate slots for the patient. Schedulers can enter appointment notes for the visit, but this information is not evaluated by the external organization to send back slots. The appointment notes are saved with the appointment that gets scheduled at the external organization and can be helpful for schedulers and clinicians who are reviewing a patient's upcoming appointments.

When schedulers select an appointment slot, the Appointment Details window appears. The slot is not held while schedulers are reviewing the appointment details. When they click Schedule, the system checks for a matching patient:

- If there is exactly one high-threshold match, the system links the patients.
- If there are no high- or low-threshold matches, the system creates a new patient and links it.
- If there are multiple high- or low-threshold matches, the system either creates a duplicate or denies scheduling depending on if the external organization is configured to allow duplicate patient creation, as described in the Allow Book Anywhere to Create Potential Duplicate Patients topic.

After the patient is linked, the system verifies that the slot is still available at the external organization and books the appointment if it is.

There are two interface errors that can appear in the Appointment Details window:

- **59190-FHIR - Book Anywhere Appointment Unschedulable.** If the slot has been taken since the scheduler first searched for openings, the scheduler is notified so they can find another slot that works for the patient.
- **59191-FHIR - Book Anywhere Patient Is Locked.** If the patient's record is locked in the remote system, the scheduler is notified that they cannot schedule the appointment.

## Book Anywhere Outgoing/Client Setup

Complete these tasks so you can schedule appointments in another organization's installation of Epic.

To schedule into an external location, you must be licensed for Care Everywhere and have the Cadence Book Anywhere license, which is included in the standard Cadence license. If you're not sure whether you have these licenses, contact your Epic representative and mention parent SLG 3550868.

Work with your Care Everywhere team and refer to the Care Everywhere: Essential Setup and Support Guide for additional information.

### Join the Book Anywhere Network

You need to join the Book Anywhere network so that other organizations can connect with you.

> **Note:** You must have Bridges security point 44-Manage Network Participation to complete this setup.

1. From the Application Access menu in text, go to Interconnect > WorldWise Admin (in February 2022 and earlier, go to One Virtual System Admin).
2. On the Book Anywhere row, press J to join the network.
3. Follow the prompts on the screen to enter the patient-facing FHIR URL for your organization and the start and end dates for your participation in the Book Anywhere network. You can find your patient-facing FHIR URL on the Communication Details tab of the My Phone Book activity (search: My Phone Book) in Hyperspace. If you don't have a patient-facing FHIR URL follow the steps listed in the Define Default URL Prefixes in the My Phone Book Activity section. When entering the URL in WorldWise Admin (or One Virtual System Admin), append "api/FHIR/STU3" to the end of the URL, such as https://<hostname>/<app>/api/FHIR/STU3.

### Create Records to Represent Scheduling Locations

For every organization that you want to schedule into, you need to create the following records:

- **Place of service (EAF).** This record represents the location at another organization that you're scheduling into from your system. It can represent the entire organization, a group of departments that are located at the same address, or a single department.
- **ID type (IIT).** For places of service that represent a subset of departments at the other organization, create an ID type where you specify those departments. If you don't have places of service that represent a subset of departments, you don't need to create ID types.

Then you need to configure Cadence System Definitions and visit types with the places of service that you're allowing for Book Anywhere scheduling. You can also specify default places of service to search in Cadence System Definitions, department records, and visit type records.

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all Book Anywhere setup tasks.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** 3397E6D0-A189-492C-AEA3-4218FDC75A06