# Appointment Communications Setup and Support Guide

**Last Updated:** July 9, 2025

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 9161D83A-CE08-4EBF-9BAE-F0E0504C425D

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Configure Patient Communication Preferences for Appointments](#configure-patient-communication-preferences-for-appointments)
- [Automatically Confirm or Cancel Appointments Based on Patient Responses](#automatically-confirm-or-cancel-appointments-based-on-patient-responses)
- [Appointment Letters](#appointment-letters)
  - [Create Content for Appointment Letters](#create-content-for-appointment-letters)
  - [Define the Appointment Letters to Print for Different Scheduling Scenarios](#define-the-appointment-letters-to-print-for-different-scheduling-scenarios)
  - [Limit the Letter Templates Available in a Department](#limit-the-letter-templates-available-in-a-department)
  - [Define the Appointment Letter for Manually Printed Reminder Letters](#define-the-appointment-letter-for-manually-printed-reminder-letters)
  - [Override the Default Cancel Letter for Specific Cancel Reasons](#override-the-default-cancel-letter-for-specific-cancel-reasons)
  - [Override Appointment Letters by Visit Type](#override-appointment-letters-by-visit-type)
  - [Show the Phone Number to Call for Appointment Information and Rescheduling in Appointment Letters](#show-the-phone-number-to-call-for-appointment-information-and-rescheduling-in-appointment-letters)
  - [Print Appointment Letters in Batch](#print-appointment-letters-in-batch)
  - [Send Appointment Letters to MyChart or by Email](#send-appointment-letters-to-mychart-or-by-email)
  - [Print Bilingual Appointment Letters](#print-bilingual-appointment-letters)
  - [Show Patients Customized Instructions for the Highest-Severity Procedure in an Appointment](#show-patients-customized-instructions-for-the-highest-severity-procedure-in-an-appointment)
  - [Show Upcoming Preadmissions and Cases in Appointment Letters](#show-upcoming-preadmissions-and-cases-in-appointment-letters)
  - [Prevent Certain Appointments from Appearing in Appointment Letters](#prevent-certain-appointments-from-appearing-in-appointment-letters)
- [Patient Appointment Notifications](#patient-appointment-notifications)
  - [Send Appointment Notifications to Patients by Email](#send-appointment-notifications-to-patients-by-email)
  - [Customize the Appointment Notification Email and MyChart Messages Sent to Your Patients](#customize-the-appointment-notification-email-and-mychart-messages-sent-to-your-patients)
  - [Use Hello World Content to Send Appointment Notifications to Patients by Text Message](#use-hello-world-content-to-send-appointment-notifications-to-patients-by-text-message)
  - [Use SmartText Records to Send Appointment Notifications to Patients by Text Message](#use-smarttext-records-to-send-appointment-notifications-to-patients-by-text-message)
  - [Block Appointment Notifications to Patients for Certain Appointments](#block-appointment-notifications-to-patients-for-certain-appointments)
  - [Automatically Set Patient Preferences for Notifications](#automatically-set-patient-preferences-for-notifications)
  - [Turn Off Certain Patient Appointment Notification Status Settings](#turn-off-certain-patient-appointment-notification-status-settings)
  - [Remove the Text Message Option for Patient Appointment Notifications](#remove-the-text-message-option-for-patient-appointment-notifications)
- [Automated Appointment Confirmation](#automated-appointment-confirmation)
  - [Determine Which Appointments Can Be Confirmed, Canceled, and Rescheduled by Text Message](#determine-which-appointments-can-be-confirmed-canceled-and-rescheduled-by-text-message)
  - [Enable Hello World Content for Appointment Confirmation Text Messages](#enable-hello-world-content-for-appointment-confirmation-text-messages)
  - [Identify the Appointments to Confirm by Text Messages from Hello World](#identify-the-appointments-to-confirm-by-text-messages-from-hello-world)
  - [Allow Reschedule Prompt After Patients Reply to Cancel Appointment for Two-Way Appointment Confirmation](#allow-reschedule-prompt-after-patients-reply-to-cancel-appointment-for-two-way-appointment-confirmation)
  - [Automatically Search for Appointments and Send Text Messages to Patients](#automatically-search-for-appointments-and-send-text-messages-to-patients)
  - [Identify the Appointments to Confirm by Automated Phone Call from a Third-Party Vendor](#identify-the-appointments-to-confirm-by-automated-phone-call-from-a-third-party-vendor)
- [Automated Appointment Calling](#automated-appointment-calling)
  - [Understand the Automated Appointment Calling Process](#understand-the-automated-appointment-calling-process)
  - [Automatically Call Patients to Notify Them of Future or Missed Appointments](#automatically-call-patients-to-notify-them-of-future-or-missed-appointments)
  - [Prevent the System from Automatically Calling an Individual Provider's Patients](#prevent-the-system-from-automatically-calling-an-individual-providers-patients)
  - [Translate Appointment Information for Automated Calling Text Messages](#translate-appointment-information-for-automated-calling-text-messages)
- [Quick Reminders and Updates](#quick-reminders-and-updates)
  - [Planning Your Quick Reminders and Updates Implementation](#planning-your-quick-reminders-and-updates-implementation)
  - [Create a Generic Queue to Hold Quick Reminders That Need to Be Sent](#create-a-generic-queue-to-hold-quick-reminders-that-need-to-be-sent)
  - [Allow Users to Send Updates](#allow-users-to-send-updates)
  - [Allow Users to Send Prewritten, Free-Text, or Both Types of Messages in Send Updates](#allow-users-to-send-prewritten-free-text-or-both-types-of-messages-in-send-updates)
  - [Send Quick Reminders and Updates by Email](#send-quick-reminders-and-updates-by-email)
  - [Use Hello World to Send Quick Reminders and Updates by Text Message](#use-hello-world-to-send-quick-reminders-and-updates-by-text-message)
  - [Use a Third-Party Vendor to Send Quick Reminders and Updates by Text Message](#use-a-third-party-vendor-to-send-quick-reminders-and-updates-by-text-message)
  - [Customize the Communication Preferences Activity for Quick Reminders and Updates](#customize-the-communication-preferences-activity-for-quick-reminders-and-updates)
  - [Show Schedulers Whether a Patient Received a Quick Reminder for an Appointment](#show-schedulers-whether-a-patient-received-a-quick-reminder-for-an-appointment)
  - [Show Schedulers and Front Desk Staff Which Patients Already Received an Update](#show-schedulers-and-front-desk-staff-which-patients-already-received-an-update)
  - [Block Certain Patients from Receiving Quick Reminders](#block-certain-patients-from-receiving-quick-reminders)
  - [Change Delivery Types for Quick Reminders and Updates for a Service Area](#change-delivery-types-for-quick-reminders-and-updates-for-a-service-area)
  - [Change the Default Offset Time for Quick Reminders](#change-the-default-offset-time-for-quick-reminders)
- [Appointment Reminders](#appointment-reminders)
  - [Create Appointment Reminder Content](#create-appointment-reminder-content)
  - [Determine the Number of Appointment Reminders to Send](#determine-the-number-of-appointment-reminders-to-send)
  - [Create a Batch Job to Send Appointment Reminders to MyChart](#create-a-batch-job-to-send-appointment-reminders-to-mychart)
  - [Create a Batch Job to Send Appointment Reminders by Email](#create-a-batch-job-to-send-appointment-reminders-by-email)
  - [Create a Batch Job to Send Appointment Reminders by Text Message](#create-a-batch-job-to-send-appointment-reminders-by-text-message)
  - [Reach All Your Patients at Once with Appointment Campaigns Bulk Outreach Action Pack](#reach-all-your-patients-at-once-with-appointment-campaigns-bulk-outreach-action-pack)

## Overview

Communication is key in every relationship, including the relationship between patients and their health care providers. Your organization has multiple options for keeping patients and care teams informed about upcoming and past appointments.

This document covers the following ways that you can notify patients about their appointments:

- **Appointment letters.** Send letters to patients by email or to MyChart, allow schedulers to manually print letters, or print letters in batches. You can specify different letter templates to use for different scenarios, such as when a new appointment has been scheduled for the patient or when a patient missed a scheduled appointment and needs to reschedule.

- **Appointment notifications.** Send emails, MyChart messages, or text messages to patients when appointments have been scheduled, changed, canceled, rescheduled, or missed.

- **Automated appointment confirmation.** Available starting in February 2023. Use Hello World's SMS gateway to send text messages to patients to remind them of their upcoming appointments and allow them to confirm, cancel, or reschedule their appointments.

- **Automated appointment calling.** Work with a third-party vendor to call patients about their upcoming or missed appointments.

- **Quick reminders and updates.** Send quick email or text message reminders and updates to patients about their appointments. Quick reminders are sent closer to the appointment time than appointment reminders.

- **Appointment reminders.** Send reminders to patients by email, text message, or MyChart messages about their upcoming appointments. Appointment reminders are sent further in advance than quick reminders.

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for each communication method.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** 9161D83A-CE08-4EBF-9BAE-F0E0504C425D