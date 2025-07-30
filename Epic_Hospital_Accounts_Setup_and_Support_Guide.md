# Hospital Accounts Setup and Support Guide

**Last Updated:** November 1, 2024

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** C4130AF3-6F7A-4889-BDBD-3B737DFB7180

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Hospital Accounts Setup: Essentials](#hospital-accounts-setup-essentials)
  - [Set Up Hospital Accounts](#set-up-hospital-accounts)
  - [Set Up the Hospital Account Advisor](#set-up-the-hospital-account-advisor)
  - [Generate Register Numbers for Public Hospitals Act Requirements for Ontario](#generate-register-numbers-for-public-hospitals-act-requirements-for-ontario)
  - [Close Cases from Within Epic](#close-cases-from-within-epic)
  - [Route Charges to the Correct Hospital Account](#route-charges-to-the-correct-hospital-account)
- [Hospital Accounts Setup: Bells & Whistles](#hospital-accounts-setup-bells--whistles)
  - [Automatically Assign Patient Classes Through the Auto-Patient Class Assignment Table](#automatically-assign-patient-classes-through-the-auto-patient-class-assignment-table)
  - [Prevent Admission Hospital Account's Account Class from Overwriting Appointment Patient Class](#prevent-admission-hospital-accounts-account-class-from-overwriting-appointment-patient-class)
  - [Set Up the Hospital Account Advisor to Work with Third-Party Systems](#set-up-the-hospital-account-advisor-to-work-with-third-party-systems)
  - [Customize Hospital Account Assignment](#customize-hospital-account-assignment)
  - [Allow Users to Quickly Open Account Activities from Registration Toolbars](#allow-users-to-quickly-open-account-activities-from-registration-toolbars)
  - [Route Charges to the Most Recent Hospital Account for the Current Hospital Account](#route-charges-to-the-most-recent-hospital-account-for-the-current-hospital-account)
  - [Use Hospital Billing Hospital Accounts for Private Pay Billing (U.K.)](#use-hospital-billing-hospital-accounts-for-private-pay-billing-uk)
  - [Protect Hospital Account Information with Break-the-Glass Checks (Denmark & Finland)](#protect-hospital-account-information-with-break-the-glass-checks-denmark--finland)
- [Hospital Accounts Support: Common Issues](#hospital-accounts-support-common-issues)
  - [Users create duplicate hospital accounts](#users-create-duplicate-hospital-accounts)
  - [Staff don't assign open hospital accounts to visits that occur in the same day](#staff-dont-assign-open-hospital-accounts-to-visits-that-occur-in-the-same-day)
  - [A user needs to change the hospital account's guarantor](#a-user-needs-to-change-the-hospital-accounts-guarantor)
- [Hospital Accounts Reporting Index](#hospital-accounts-reporting-index)

## Overview

Hospital accounts provide a way for your organization to store financial and billing information for each patient. Preparing your system to assign hospital accounts appropriately to different types of patient encounters helps ensure accurate and efficient billing.

For front-end staff who collect a lot of patient information each time they register a patient, selecting a hospital account or creating a new one can slow down their work. The Hospital Account Advisor helps them assign the appropriate hospital account based on a patient's upcoming care. Taking the guesswork out of hospital account assignment helps registrars work quickly and accurately, and, later, saves billing staff time by providing the information that they need.

### Across your organization

Registrars or other staff who register patients create hospital accounts at scheduling, pre-registration, or check-in so that the hospital account can store charges as soon as patient care begins. In the Emergency and Labor and Delivery departments, where patients often need urgent care, you can set up the system to automatically create a hospital account when a patient arrives. Because a registrar doesn't have to manually create a hospital account, patient care can begin immediately and the hospital account can store accurate charges.

Later, billing staff apply charges and collect reimbursement based on hospital accounts. In Epic, hospital account information is stored in the HAR master file. For more information about using hospital accounts as a part of your billing workflows or about maintaining the HAR master file, refer to the Hospital Account Maintenance Setup and Support Guide.

### In the Foundation System

Hospital accounts are fully configured in the Foundation System. The Foundation System setup minimizes the amount of time and effort registrars must spend assigning an accurate hospital account to an encounter or creating a new one.

Log in to the Foundation Hosted environment to explore the hospital accounts setup. The ADT Administrator (ADTADM) and the Cadence Administrator (ESADM) users have the security necessary to see and edit hospital account settings.

## How It Works

Hospital accounts play a central role in Epic's revenue cycle. A hospital account stores complete data about a patient's guarantor, coverages, and patient class for a certain encounter. It also tracks charges for services and resources that a patient uses during that encounter. Assigning a hospital account to each encounter helps ensure that billing and reimbursement processes work effectively.

Your staff can link hospital accounts to recurring or non-recurring encounters. Recurring hospital accounts let charges from recurring visits start to age, but your organization still collects payment frequently enough to keep account balances at a manageable level. When you use recurring hospital accounts, the system assigns a single parent hospital account to the entire set of encounters. Then, child hospital accounts apply to smaller groups of encounters within the whole set. Later, billing staff use the child hospital account numbers to distinguish charges that should be billed together. For example, using a recurring hospital account would prevent your organization from needing to bill a radiation therapy patient after each visit. Instead, staff could collect payment at regular intervals for sets of visits grouped by child hospital accounts.

Sometimes, the same hospital account should be applied to multiple encounters, such as a patient who has multiple appointments in various departments on one day. The Hospital Account Advisor indicates to registrars and other front-end staff whether they should create a new hospital account or assign an existing hospital account. The Hospital Account Advisor uses a number of criteria to determine if an existing hospital account applies to a new encounter, but it cannot use payer information. Therefore, if you want to consider payer information to determine which hospital account applies to an encounter, don't turn on auto-assignment. If you want to use payer information as criteria in hospital account assignment, you should also instruct your staff to look at the relevant payers for each encounter to determine if the Hospital Account Advisor's recommendation is appropriate.

## Hospital Accounts Setup: Essentials

In this section, we'll cover everything that you need to do to start using hospital accounts. This includes what you need to do to prepare your facility to use hospital accounts, how you can set up the Hospital Account Advisor at your organization, and how to configure hospital accounts to match our recommendations.

### Set Up Hospital Accounts

Before using hospital accounts at your organization, you need to consider how your organization bills different types of encounters and set up your system to reflect those practices. Whether an encounter qualifies for a recurring or a non-recurring hospital account depends on the patient class, so you must associate each patient class with either recurring or non-recurring accounts. Also determine which users will create hospital accounts and in which departments each encounter should automatically link to a new hospital account.

Epic recommends that you configure most of these settings at the service area level. For departments that require alternative setup, you can specify settings at the revenue location or department level and they will override any more general settings you create.

#### Define Hospital Account Type Based on Patient Class

To determine whether a hospital account should be non-recurring or recurring, the system looks to the patient class associated with an encounter. You must specify whether each patient class should trigger a recurring or a non-recurring hospital account at the service area level.

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all hospital account features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** C4130AF3-6F7A-4889-BDBD-3B737DFB7180