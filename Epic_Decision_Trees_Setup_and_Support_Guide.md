# Decision Trees Setup and Support Guide

**Last Updated:** July 18, 2025

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 73DD2CEF-9217-4068-BB6E-B73543FF0D49

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Decision Trees Setup and Support Guide](#decision-trees-setup-and-support-guide)
  - [Decision Trees Strategy](#decision-trees-strategy)
    - [Determine Whether to Use Decision Trees or Scheduling Questionnaires](#determine-whether-to-use-decision-trees-or-scheduling-questionnaires)
    - [Designing Decision Trees](#designing-decision-trees)
    - [Maintaining Decision Trees](#maintaining-decision-trees)
  - [Decision Trees Setup: Essentials](#decision-trees-setup-essentials)
    - [Create a Decision Tree](#create-a-decision-tree)
    - [Learn About the Types of Decision Tree Nodes](#learn-about-the-types-of-decision-tree-nodes)
    - [Create SmartText Instructions for Decision Tree Nodes](#create-smarttext-instructions-for-decision-tree-nodes)
    - [Map Indications to Request Entry Decision Trees](#map-indications-to-request-entry-decision-trees)
    - [Define the Financial Decision Tree for Your Organization](#define-the-financial-decision-tree-for-your-organization)
    - [Define the Patient Self-Triage Decision Trees for Your Organization](#define-the-patient-self-triage-decision-trees-for-your-organization)
    - [Make an Appointment Entry Decision Tree Available at the Visit Type or Panel Level](#make-an-appointment-entry-decision-tree-available-at-the-visit-type-or-panel-level)
    - [Define the Book Anywhere Decision Tree for Your Organization](#define-the-book-anywhere-decision-tree-for-your-organization)
    - [Show the Results of an Appointment Entry Decision Tree to Schedulers](#show-the-results-of-an-appointment-entry-decision-tree-to-schedulers)
    - [Show the Results of Scheduling Decision Trees to Clinicians](#show-the-results-of-scheduling-decision-trees-to-clinicians)
    - [Show the Results of a Patient Self-Triage Decision Tree to Providers](#show-the-results-of-a-patient-self-triage-decision-tree-to-providers)
  - [Decision Trees Setup: Bells & Whistles](#decision-trees-setup-bells--whistles)
    - [Make an Appointment Entry Decision Tree Available at the Department or System Level](#make-an-appointment-entry-decision-tree-available-at-the-department-or-system-level)
    - [Limit How Many Times a Patient Can Start a Self-Triage Decision Tree in 24 Hours](#limit-how-many-times-a-patient-can-start-a-self-triage-decision-tree-in-24-hours)
    - [Show Risk Score Information in Decision Trees](#show-risk-score-information-in-decision-trees)
    - [Show Related Orders and Appointments Requests in Decision Trees](#show-related-orders-and-appointments-requests-in-decision-trees)
    - [Use Rules to Evaluate How Many Orders Are Linked to an Appointment](#use-rules-to-evaluate-how-many-orders-are-linked-to-an-appointment)
    - [Use the Results of a Nested Decision Tree to Drive Other Actions](#use-the-results-of-a-nested-decision-tree-to-drive-other-actions)
    - [Use Nested Decision Trees to Give Patients Options in Self-Triage](#use-nested-decision-trees-to-give-patients-options-in-self-triage)
    - [Associate Self-Triage Decision Tree Orders With a Department](#associate-self-triage-decision-tree-orders-with-a-department)
    - [Let Patients Request an Appointment from Self-Triage](#let-patients-request-an-appointment-from-self-triage)
    - [Bundle Orders with Appointments That Patients Can Schedule Together](#bundle-orders-with-appointments-that-patients-can-schedule-together)
    - [Send Self-Triage Decision Trees from Appointment Desk](#send-self-triage-decision-trees-from-appointment-desk)
    - [Define an Expected Path Through Appointment Entry Decision Trees](#define-an-expected-path-through-appointment-entry-decision-trees)
  - [Decision Trees Support: Ongoing Tasks](#decision-trees-support-ongoing-tasks)
    - [View a Decision Tree](#view-a-decision-tree)
    - [Edit a Released Decision Tree](#edit-a-released-decision-tree)
    - [Search Within a Decision Tree](#search-within-a-decision-tree)
    - [Copy and Paste Nodes and Connections](#copy-and-paste-nodes-and-connections)
    - [Copy a Decision Tree Contact to a New or Existing Contact](#copy-a-decision-tree-contact-to-a-new-or-existing-contact)
    - [View the Decision Making Path for a Decision Tree](#view-the-decision-making-path-for-a-decision-tree)
    - [Test Drive a Decision Tree](#test-drive-a-decision-tree)
    - [Mark a Decision Tree As Reviewed](#mark-a-decision-tree-as-reviewed)
    - [View the Records That Are Linked to a Decision Tree](#view-the-records-that-are-linked-to-a-decision-tree)
    - [View the Audit Trail for Changes Made to a Decision Tree](#view-the-audit-trail-for-changes-made-to-a-decision-tree)
    - [Find Decision Tree Rules and Questionnaires That Contain Certain Question Records](#find-decision-tree-rules-and-questionnaires-that-contain-certain-question-records)

## Decision Trees Setup and Support Guide

Decision trees help schedulers who work in complex specialty areas to schedule the right visit with the right provider and resources. Decision trees can handle advanced logic to offer a consistent scheduling experience for both schedulers and patients. Decision trees are typically built as a part of a larger project. When planning decision tree build, make sure to consider the other relevant pieces of functionality that are supported by decision tree build, such as templates, blocks, visit types, ordering workflows, and direct and ticket scheduling in MyChart. For more information about our recommendations for these related records, refer to the Transitioning to System-Guided Scheduling document.

There are several types of decision trees:

- **Appointment Entry.** Use appointment entry decision trees with your visit types to show a decision tree to a scheduler when she enters a particular visit type in Make Appointment and to a patient when he selects a particular visit type in MyChart. Patients can use them in MyChart direct scheduling and ticket scheduling, in the redesigned open scheduling widget starting in November 2021, and in the open scheduling wizard and when scheduling with a new provider in MyChart starting in February 2022.

- **Book Anywhere.** Use Book Anywhere decision trees to process requests from external locations to schedule appointments at your organization. For more information, refer to the Book Anywhere Setup and Support Guide.

- **Financial.** Use financial decision trees to perform financial screening for a patient in an appointment request before you schedule a visit for the patient. For more information about financial screening, refer to the Perform Financial Screening in Appointment Requests topic.

- **Request Entry.** Use request entry decision trees in appointment requests to guide pre-scheduling workflows. For more information about appointment requests, refer to the Use Appointment Requests for Intake topic.

- **Patient Self-Triage.** Use self-triage decision trees to help direct patients to the right level of care, such as showing them instructions or helping them schedule a procedure.

Here is a scheduler's view of an appointment entry decision tree that opened when she selected the Consult - Dermatology visit type in Make Appointment:

Refer to this table for a comparison of the features offered by appointment entry decision trees and scheduling questionnaires:

| Feature | Decision Trees | Scheduling Questionnaires |
|---------|----------------|---------------------------|
| Complex logic | Decision trees support complex branching logic in a visual editor that's similar to drawing a flowchart. | Scheduling questionnaires can have conditional questions, but it can be difficult to build and maintain that logic in the Questionnaire Editor. |
| Use data that's already in the system | You can add rules to a decision tree that pull information from the system. For example, you might create a rule for a decision tree to follow a certain branch of logic for pediatric patients. | To do something similar with scheduling questionnaires, you need to create a question to capture the information you need and then build conditions off of the answer. |
| Schedule with the right provider | Decision trees can recommend specific providers, subgroups, or pools for scheduling that automatically populate in Make Appointment. | Scheduling questionnaires can only show instructions to a scheduler about which provider to schedule the appointment with. It's up to the scheduler to enter the correct provider in Make Appointment. |
| Rich text formatting | Decision trees support showing RTF or plain text instructions to schedulers. | Scheduling questionnaires support only plain text instructions. |
| Show questions to schedulers as they go | The questions in a decision tree appear one at a time for a scheduler to answer as the system evaluates the logic in the decision tree for what needs to happen next. | The questions in a questionnaire appear all at once. Questions can be enabled or disabled based on the answers to other questions in the questionnaire. |
| Combine questionnaires from different levels of the facility structure | Decision trees cannot be combined like scheduling questionnaires can. Instead, you can build logic for the situations you need to support and reuse the common questions in each situation. You can also use a decision tree within another decision tree. | The system can combine questionnaires from different levels of the facility structure and present them at once to a scheduler. You might use this when additional questions need to be asked for a visit type when it is being scheduled in a certain department. |
| Change answers after filing | Because decision trees drive scheduling, schedulers cannot edit the answers to a decision tree after it has been filed. | Schedulers can edit the answers to a scheduling questionnaire after it has been filed. |
| Share with MyChart | Decision trees are supported in MyChart in direct scheduling and ticket scheduling, in the redesigned open scheduling widget starting in November 2021, and in the open scheduling wizard and when scheduling with a new provider in MyChart starting in February 2022. | Scheduling questionnaires can be used in Cadence and MyChart. |

> **Note:** Decision trees cannot be imported. You must build them in Hyperspace.

### In the Foundation System

The Foundation System has examples of appointment entry decision trees for many specialty areas that you can use as a starting point for your organization's build. To see the available appointment entry decision trees, log in to the Foundation Hosted environment as your organization's scheduling administrator (ESADM), open the Appointment Entry Decision Tree editor, and press enter to search for all records. To use Foundation System decision trees as a starting point for your organization's build, your Epic representative can help you migrate the decision trees into your own environment.

You can also try out decision trees in the Foundation System to see the functionality in action:

- **1170000004-ES Annual Wellness** is used to determine whether a patient's annual wellness visit should use a Physical, Medicare Annual Wellness, or Welcome to Medicare visit type. The decision tree uses a rule to check the system for the presence of Medicare coverage or whether the patient had an appointment in the last year. If no coverage or appointments in the last year are found, the user is presented with several questions to confirm the findings. For example, if the patient is over 65 and the rule doesn't find Medicare in the system, then it asks the user in case the coverage hasn't been added to the patient's record yet. This decision tree also includes an example of a rule-based SmartText, 17984-ES Previous Medicare Visit Info. The SmartText shows schedulers previously completed or arrived Medicare visits the patient had scheduled at the facility to help them understand the workflow of the decision tree and when they could schedule the next Medicare visit based on Medicare requirements. To try out this tree, log in to the Foundation Hosted environment as your organization's front desk user (ESDESK) in the EMC Family Medicine department. Click Make Appt on a patient's Appointment Desk and select a visit type of 1005-Physical to launch the decision tree.

- **1170000002-ES Wound Check Preprocedure Resource** appears when schedulers select a wound check visit type, which sometimes requires a preprocedure nurse to be present during the visit. The decision tree asks the scheduler if a preprocedure nurse is needed for the appointment. If the scheduler answers Yes, the system adds a Preprocedure Nurse to the appointment as an additional resource. To try out this tree, log in to the Foundation Hosted environment as your organization's front desk user (ESDESK) in the EMH Wound Care department. Go to Make Appt on the patient's Appointment Desk and select a visit type of 17106-Hospital Wound Check. Choosing this visit type launches the decision tree.

- **1170000006-ES Priority Patient Tag** allows schedulers to schedule office visits for Priority patients into New Patient or Physical blocked slots so the patient can be seen more quickly. To try out this tree, log in to the Foundation Hosted environment as your organization's front desk user (ESDESK) in the EMC Family Medicine department. Open registration for a patient, go to the Additional Demographics form, and enter Priority in the Patient type(s) field. Then schedule an office visit for that patient and select a visit type of 1006-Office Visit to launch the decision tree.

- **1170000012-ES Pulmonary Function Test (PFT) Duration** uses the Replace option in the Replace Visit node to change the visit length to match the PFT type that the scheduler selects. This allows the scheduler to book the correct amount of time for the appointment automatically. To try out this tree, log in to the Foundation Hosted environment as your organization's front desk user (ESDESK) in the EMC Pulmonary department. Click Make Appt on a patient's Appointment Desk and select a visit type of 17098-Pulmonary Function Test to launch the decision tree.

- **1170000008-ES Multiple Visits** asks the scheduler questions to determine how many visits to schedule and which visit types to use. The decision tree then adds a panel with the appropriate visits. To try out this tree, log in to the Foundation Hosted environment as your organization's front desk user (ESDESK) in the EMH Interventional Cardiology department. Click Make Appt on a patient's Appointment Desk and select a visit type of 17113-New Patient Interventional Cardiology to launch the decision tree.

There are also examples of request entry decision trees in the Foundation System, including:

- **1170000005-ES Physician Referral Review** for situations where schedulers are doing intake on referrals from physicians. This tree helps determine which visit type to use for a consultation with the provider's specific subspecialty.

- **1170000007-ES New Patient Intake** determines whether a patient needs a new patient visit or if they should be scheduled for a different visit type because they have been seen recently.

- **1170000003-EHS Neurology Appointment Request** includes an example of a nested decision tree that outputs a score. The decision tree 1170000013-Headache Scoring is nested inside the parent tree. The child tree asks questions about the patient's headache symptoms and assigns scores based on the answers. If the total score meets or exceeds a threshold, the parent tree adds an Urgent tag to the appointment request so that the patient can be scheduled sooner.

To see the available request entry decision trees, log in to the Foundation Hosted environment as your organization's scheduling administrator (ESADM), open the Request Entry Decision Tree editor, and press enter to search for all records.

**Patient Self-Triage Decision Trees in Foundation System**

The Foundation System includes self-triage decision trees for more than 40 symptoms. This content is designed to be a starting point that your clinical team should review and adapt to the practices, preferences, and protocols that make sense for your organization. If you have connected to the Content Subscription Platform, you can subscribe to this content subscription Turbocharger package to receive updates automatically when they're available. For more information about importing these records, refer to the 284329-Decision Trees for MyChart Self-Triage topic.

To view this content as a patient, log in to the Foundation Hosted environment as your MyChart patient and go to Health > Symptom Checker. To view the decision tree records themselves, log in as your MyChart administrator (MYCADM) and go to the Patient Self-Triage Decision Tree editor (Search: Patient Self-Triage Decision Tree). For a full list of symptoms built in Foundation System, refer to the MyChart Symptom Checker and E-Visit Catalog.

## Decision Trees Strategy

### Determine Whether to Use Decision Trees or Scheduling Questionnaires

When you need to ask schedulers questions before an appointment is scheduled to capture information for the appointment or determine what kind of appointment to schedule, you can either use scheduling questionnaires or appointment entry decision trees. Both approaches have their advantages.

If you already use scheduling questionnaires, consider which of your existing questionnaires would work better as decision trees. In particular, questionnaires that ask schedulers to choose an answer and then you want the system to take a certain action (such as changing the visit type, setting a tag, or modifying the appointment length) based on that answer would work well as decision trees. Questionnaires that ask schedulers questions for documentation purposes and don't require any follow-up actions might work better to remain as questionnaires.

If you're just getting started with guided scheduling, decision trees offer more sophisticated functionality, so they are the preferred approach for new build.

### Designing Decision Trees

Here are some guidelines to keep in mind when designing decision trees:

**Be judicious with questions.** Don't ask questions that you don't need the answers to or that don't affect how the appointment gets scheduled. Remember that every question slows down the scheduling process.

**Ask the most important questions first.** If you put the most important questions at the beginning of the decision tree, you ensure that schedulers answer them even if they get interrupted or decide to stop answering questions partway through the tree.

**Keep it simple.** Decision trees can handle complex logic, but complex trees take longer to maintain, troubleshoot, and explain to users. Build the simplest version that meets your requirements.

**Make the tree resilient.** Don't create trees that will break if individual master file records (such as providers, visit types, or departments) are inactivated. For example, instead of specifying a particular provider by name, you might specify a pool that could contain multiple providers.

**Use rules to avoid asking unnecessary questions.** If the system already knows something about the patient, use a rule to pull that information into the tree instead of asking the scheduler to enter it again.

**Test your trees thoroughly.** Use the Test Drive functionality in the decision tree editor to make sure the tree behaves as expected for a variety of scenarios.

**Think about MyChart scheduling.** If patients will use your decision tree in MyChart, make sure that the questions make sense for patients to answer and that the tree provides appropriate instructions for patients when needed.

### Maintaining Decision Trees

Make sure you know your organization's record naming and numbering conventions. This is especially important if you have a large decision tree scope. Epic's recommended convention is to name questions and questionnaires as `<Application> <Specialty> <Description>`, such as ES GAS New Patient for a scheduling questionnaire used by the gastroenterology department. Find additional information about naming and numbering conventions in the Epic Style Guide Master File Naming and Numbering Conventions document.

Reuse records in your decision trees whenever possible for easier maintenance. SmartTexts, visit types, decision trees, questionnaires, questions, and rules can all be reused in decision trees. When you reuse records instead of creating duplicates, it's easier to change your build later.

If you're migrating your scheduling questionnaires to decision trees, you can reuse your questionnaires in your decision trees. Note that any visit type conditions, such as changing the visit type, in the questionnaire do not apply when the questionnaire is used in a decision tree. Questionnaire conditions, such as disabling certain questions based on the answer to other questions, do carry over to the decision tree.

Whenever possible, create trees that you can embed into other trees. This modular strategy speeds up build and makes maintenance easier.

## Decision Trees Setup: Essentials

In this section, we'll cover everything that you need to do to start using decision trees. This includes what you need to do to make decision trees available to your schedulers and how to configure decision trees to match our recommendations.

> **Important:** All of these instructions assume you are editing a decision tree in a non-production environment or an unreleased decision tree in your production environment. Refer to the Edit a Released Decision Tree topic for information about the potential consequences of editing released decision trees in your production environment.

### Create a Decision Tree

You build decision trees by creating nodes for things you want the decision tree to do, such as ask a question or return the value of a rule, and drawing connections between the nodes that define the logic you want the system to follow.

In the decision tree editors, nodes are represented by boxes and connections are represented by arrows. You can hover over a node to view the connection points that you can drag to draw an arrow between two nodes.

Some nodes support showing instructions to the scheduler. You can write the instructions directly in the node or create reusable SmartText records for the instructions in the Appointment Entry Tree Instructions Editor and Request Entry Tree Instructions Editor, which is used for both financial and request entry decision trees. We recommend using SmartTexts whenever possible to simplify maintenance.

#### Considerations

**Be consistent** with how you arrange nodes and connections in the decision tree editors. For example, you might always put the default connection for a node on the right. It's also a good idea to add all of a node's connections before selecting the default connection.

**The default connection** determines the action that takes place if no other connections are satisfied. We recommend always using default connections so you avoid dead ends in a tree's logic, especially for questions that have a custom list of answers or are networked to an item. If the custom list or item changes and you don't update your decision tree to account for the change, the default connection is your fall back.

**Tips for using questions and questionnaires in decision trees:**

- Use a question when you need a scheduler to enter or confirm something. If you already have the answer in the system, use a rule to pull it in instead of duplicating work for the scheduler. For example, you can use a rule to get the patient's sex from the system instead of asking the scheduler to enter it.
- When a question has five or fewer answers, create quick buttons for those answers. They look nice in the decision tree and make answering the question faster for schedulers.
- Don't show the comment field for a question to schedulers unless you're planning to report on the text schedulers enter.
- Avoid including a question in a request entry decision tree if schedulers will need to answer it again when scheduling the appointment.
- Use questions instead of questionnaires unless the tree's branching logic depends on the answers to multiple questions.

#### Create a Decision Tree Record

1. In Hyperspace in your build environment, open the decision tree editor for the type of tree you want to create by searching for:
   - Appointment Entry Decision Tree
   - Book Anywhere Decision Tree
   - Financial Decision Tree
   - Request Entry Decision Tree
   - Patient Self-Triage Decision Tree

2. Select the Create tab and enter and name and ID for your decision tree.

3. Complete the following information on the Basic Information tab:
   - **Synonyms.** Enter synonyms for the decision tree. These can help you look up the decision tree later.
   - **Owners.** Enter the users who are responsible for maintaining this decision tree. This field does not restrict who can edit the decision tree. It's only a way to know who to contact with questions.
   - **Notes.** Enter notes about what this decision tree is used for.
   - For patient self-triage decision trees, enter a patient-friendly name and description.

4. When you're ready to test your decision tree, click **Test Release**. This button is available starting in February 2019 and allows you to link the decision tree to other records for testing. In earlier versions, click **Release Contact** to test the decision tree and then create a new contact if you need to make any changes.

5. When you're ready to release the decision tree and move it to production, click **Release Contact**.

6. For request entry decision trees, select the **Allow this decision tree to be manually searched** check box to allow schedulers to search for this decision tree in the Decision Tree Search section of the Appointment Request activity. If you don't select this check box, the decision tree only appears in the Decision Tree Search section as a suggested decision tree if you map the decision tree to diagnoses and the patient has one of the mapped diagnoses entered in the Indications section of the Appointment Request activity.

#### Add Nodes to a Decision Tree

Select the Decision Tree tab in the decision tree editor and click **Add Node**, or right-click the workspace and choose **Add Node**.

#### Add Connections Between Nodes

Connections determine the logic of how a scheduler moves through a decision tree. Hover over a node to view the connection points. Click and drag one of the points to connect it to another node. All node connections can evaluate a rule except for question nodes.

- For appointment entry decision trees, choose from **5003-Appointment Entry Begin** context rules. In Epic 2017 and earlier, this is the Visit Type Scheduling Restriction context.
- For Book Anywhere decision trees, choose from **5003-Appointment Entry Begin** and **5060-Book Anywhere** context rules.
- For financial and request entry decision trees, choose from **5008-Appointment Request** context rules.
- For patient self-triage decision trees, choose from **32002-MyChart Patient Self-Triage** rule context rules.
- Question nodes evaluate the question answers, and questionnaire nodes evaluate the **5001-Questionnaire** context rules from the selected questionnaire for all decision trees except patient self-triage decision trees.
- Patient self-triage decision trees evaluate questionnaire nodes using the **32002-MyChart Patient Self-Triage** rule context rules regardless of the kind of connection node, and you must use the **32980-Decision Tree Question Answer** property when building rules for this kind of tree.

The connection logic options that are available depend on the type of node the connection is coming from.

By default, the system evaluates connections in the order you created them. You can change this order by selecting the node and rearranging the connections in the Connection Ordering section. The system evaluates the list of connections in the order they are listed and follows the path for the first true connection. If no connection evaluates to true, the system follows the default connection.

### Learn About the Types of Decision Tree Nodes

This section describes all the nodes you can add to decision trees and what they do.

#### Add Appointment Request

*Applies only to patient self-triage decision trees.*

Allows patients to create an appointment request for a visit they need to schedule. The request is added to your organization's schedule orders/appointment request workqueue for schedulers to handle. The patient can optionally attach files to the request, such as lab results, in supported file formats (PDF, JPEG, PNG, DOCX, TXT, and RTF).

You can specify which providers and provider pools the request can be sent to. If you don't specify anything, the appointment request is sent to the patient's PCP.

When setting up this node, think carefully about which providers and pools are appropriate destinations for appointment requests that come from this decision tree. Avoid sending appointment requests to providers who don't normally handle scheduling for their own appointments.

For more information about appointment requests, refer to the Use Appointment Requests for Intake topic.

To configure an Add Appointment Request node:

1. In Hyperspace, open the decision tree editor, select the **Decision Tree** tab, and click **Add Node**.
2. Fill out the node details:
   - In the **Type (I LQL 1200)** field, enter **Add Appointment Request**.
   - In the **Request Type (I LQL 32450)** field, enter the request type for the appointment request.
   - In the **Pool (I LQL 32451)** field, enter the pool to send the appointment request to. This overrides provider-specific routing.
   - In the **Provider (I LQL 32452)** field, enter the provider to send the appointment request to.
   - In the **Allow File Attachments (I LQL 32453)** field, enter **1-Yes** to allow patients to attach files to the appointment request or **0-No** to not allow file attachments.
3. Make sure to set up a connection to the node from other nodes in the tree.

#### Add Order

*Applies only to patient self-triage decision trees.*

Adds an order to the patient's chart. The system creates a MyChart Self-Triage encounter for the order if an encounter for the current date doesn't already exist.

The order is routed to providers based on the following logic:
- If the **Provider** field is set to a specific provider, the order is routed to that provider.
- If the **Provider** field is blank but the **Pool** field is set to a specific pool, the order is routed to the specified pool.
- If the **Pool** field is also left blank, the order is routed to the patient's PCP.
- If there is no PCP for the patient or their PCP is not a valid destination, the order is routed to the department specified in the **Default Department (I WDF 13540)** setting. Within that department, the order is routed to the pool set in the **Unsigned Orders Pool (I DEP 15001)** setting.
- If not routed according to any of the previous criteria, orders are routed to the provider specified in the **Default Provider (I WDF 13530)** setting.

To configure an Add Order node in a patient self-triage decision tree:

1. In Hyperspace, open the decision tree editor, select the **Decision Tree** tab, and click **Add Node**.
2. Fill out the node details:
   - In the **Type (I LQL 1200)** field, enter **Add Order**.
   - In the **Order (I LQL 32400)** field, enter the procedure that will be ordered. These are records in the Procedures (EAP) master file.
   - In the **Action (I LQL 32401)** field, choose whether the system should sign or pend the orders. Pended orders get sent to the authorizing provider's My Unsigned Orders folder in In Basket. Pended orders are signed on the Patient Self-Triage encounter.
   - In the **Associated Diagnoses (I LQL 32404)** field, determine which diagnoses to associate with the order when it gets generated. This field is available starting in August 2020.
   - In the **Specialty (I LQL 32402)** field, enter a specialty.
   - In the **Pool (I LQL 32403)** field, enter a pool.
3. Make sure to set up a connection to the node from other nodes in the tree.

#### Add Panel

*Applies only to appointment entry and request entry decision trees. Note that this node type is not supported in new provider scheduling in versions prior to February 2022 or open scheduling.*

For appointment entry, this node adds a panel to Book It when the scheduler applies the decision tree. For request entry, this node adds a panel to the Visit section of the Appointment Request activity. You can optionally choose to:

For appointment entry, change the length for each visit type in the panel:
- **Add or subtract time.** Enter the number of minutes in multiples of 5.
- **Add Slot Lengths** (starting in November 2023). Enter the number of default slot lengths, between 1-100 slots. A provider's default slot length is set in Slot Length (mins) field on the settings tab of the provider's template or by following the path Epic button > Admin > Schedule Admin > Templates > Rel Date/Defaults.
  - This option is especially useful when scheduling visits that you need to extend, but your providers each have different slot lengths on their templates.
  - Your providers might have slots lengths on their template that do not match their default slot length, so use caution when using this option with those providers. A scheduler could end up splitting the slots on a provider's scheduler if the extended visit length does not match the slots on the provider's schedule, in which case the other half of the split slot can't be scheduled.
  - Here is an example of how this option works: Dr. Roberts has a Default Slot Length of 10 minutes and Dr. Chavez has a Default Slot Length of 15 minutes. The visits added in a panel by the decision tree are both 30 minutes. If you use an Add Panel node that adds 2 slot lengths, when scheduled with Dr. Roberts the final length of each visit in the panel is now 50 minutes and when scheduled with Dr. Chavez the final length of each visit in the panel is 60 minutes.
- **Multiply** (starting in November 2023). Enter the number of times to multiply the length, between 2-10 times its calculated length. The calculated length of a visit is affected by Visit Type Modifiers.
  - This option is useful if you need to extend the length of a visit in large increments depending on patient rules. For example, if you have a patient coming in for an annual physical, but they are also a new patient, you could have a decision tree automatically multiply the length of the physical by 3 times to allow the provider enough time to gather any required new patient paperwork.
  - Here is an example of how this option works: Say the visits in the panel added by the decision tree are each 15 minutes. When scheduled with Dr. Roberts who has a visit type modifier to add 5 minutes on both visit types, the new calculated length for each is 20 minutes. If you have an Add Panel node that multiplies the visits in the panel by 3, the final length for each visit will be 60 minutes.

For appointment entry, replace the visit type the scheduler originally entered in Book It with the panel.
For appointment entry, don't launch the decision tree or questionnaire that is linked to the panel when this decision tree is applied.
For appointment entry and request entry, include instructions to tell schedulers what they should do next and how they should communicate the decision or next steps to the patient.

#### Add Tag

*Applies only to appointment entry and request entry decision trees.*

Sets a tag for the patient.

##### Use Tags to Schedule Patients into Certain Visit Type Blocks

Tags can allow a patient to be scheduled into any visit type block that is mapped to the tag. For more information about tags and blocks, refer to the Restrict Time in Schedules for Specific Visit Types Using Blocks topic. For example, the Foundation System includes a tag for Priority patients that allows office visits for these patients to be scheduled into New Patient and Physical blocks so they can be seen sooner.

##### Use Tags to Request Resources for Appointments

Tags can tell the system to automatically request a resource for an appointment. For more information about tags and resource requests, refer to the Automatically Request Additional Resources for Departments and Visit Types topic.

##### Use Tags to Prevent Agent Conflicts or Override Patient Prep and Recovery Time

You can use tags to determine whether a particular agent associated with a visit type is used for a given appointment. Or, use tags to determine whether a patient prep and recovery time override applies to a given appointment. Use property **98238-Tags** in your **5009-Appointment Agent & Patient Prep and Recovery** rule. Refer to the Prevent Agent Conflicts and Allow Time for Patients to Prepare for and Recover from Appointments topics for more information.

##### Use Tags to Show Custom Warnings During Scheduling

If a scheduler needs to be warned during scheduling about patients who have a certain tag, you can create a custom rule that checks a patient's tags and shows a warning if certain conditions are met. Use property **98238-Tags** in a **5005-Appointment Entry Custom Check**, **5006-Appointment Entry Provider Check**, or **5007-Appointment Entry Date Check** rule. Refer to the Show Custom Warnings Based on Rules During Scheduling topic for more information.

##### Use Tags to Change the Patient Instructions for an Appointment

You can use tags to determine which patient instructions SmartText is used for an appointment. Use property **98238-Tags** in your **5040-Visit Type Patient Instructions** rule. Refer to the Include Scheduling and Patient Instructions topic for more information.

##### Use Tags in Smart Pools

You can use tags to determine whether a row in the Pool Definition table for a Smart Pool gets evaluated for a particular visit. Use property **98238-Tags** in your **5050-Pool Search Inclusion Rule** rule. Refer to the Organize Pools of Providers or Resources topic for more information.

##### Use Tags to Set the Telehealth Mode for an Appointment

Starting in May 2023, using the Set Telehealth Mode node is recommended to set a telehealth mode for an appointment instead of doing this setup to use a tag. The node is simpler to set up and you can do more with it.

You can use tags to identify the care setting in which an appointment takes place. To do so, you must map telehealth modes to tags in your system. Note that applying telehealth modes using decisions trees works for both appointments scheduled in Hyperspace and in MyChart starting in November 2020. In previous versions, this decision tree configuration doesn't apply to MyChart scheduling.

1. In Hyperspace, open **Cadence System Definitions** and go to the **Scheduling > Telehealth** form.
2. In the **Telehealth Settings** table, map telehealth modes to decision tree tags by entering values for each on the same row in the **Telehealth Mode (I SDF 12200)** and **Tag (I SDF 12210)** columns, respectively.
3. If your system should use a specific patient arrival location whenever it sets a telehealth mode using a decision tree, enter that arrival location in the **Override Arrival Location (I SDF 12220)** column in the same row.

#### Add Task

*Applies only to request entry decision trees.*

Adds a task to the Tasks section of the Appointment Request activity to indicate there is work to be done before the visit can be scheduled. For more information about tasks, refer to the Use Tasks to Identify When a Request Is Ready to Be Scheduled topic.

#### Add Visit

*Applies only to appointment entry and request entry decision trees. Note that this node type is not supported in new provider scheduling in versions prior to February 2022 or open scheduling.*

For appointment entry, this node adds a visit to Book It when the scheduler applies the decision tree. For request entry, this node adds a visit to the Visit section of the Appointment Request activity. You can optionally choose to:

For appointment entry, change the length of the visit:
- **Add or subtract time.** Enter the number of minutes in multiples of 5.
- **Replace.** Enter any amount of time as the final visit length. Overrules every other change option. Open decision tree **1170000012-ES Pulmonary Function Test (PFT) Duration** tree in the Foundation System to see an example of the Replace option.
- **Add Slot Lengths** (starting in November 2023). Enter the number of default slot lengths, between 1-100 slots. A provider's default slot length is set in **Slot Length (mins)** field on the settings tab of the provider's template or by following the path Epic button > Admin > Schedule Admin > Templates > Rel Date/Defaults.
  - This option is especially useful when scheduling visits that you need to extend, but your providers each have different slot lengths on their templates.
  - Your providers might have slots lengths on their template that do not match their default slot length, so use caution when using this option with those providers. A scheduler could end up splitting the slots on a provider's scheduler if the extended visit length does not match the slots on the provider's schedule, in which case the other half of the split slot can't be scheduled.
  - Here is an example of how this option works: Dr. Roberts has a Default Slot Length of 10 minutes and Dr. Chavez has a Default Slot Length of 15 minutes. The visit added by the decision tree is 30 minutes. If you use an Add Visit node that adds 2 slot lengths, when scheduled with Dr. Roberts the final length of the visit added is now 50 minutes and when scheduled with Dr. Chavez the final length of the visit added is 60 minutes.
- **Multiply** (starting in November 2023). Enter the number of times to multiply the length, between 2-10 times its calculated length. The calculated length of a visit is affected by Visit Type Modifiers.
  - This option is useful if you need to extend the length of a visit in large increments depending on patient rules. For example, if you have a patient coming in for an annual physical, but they are also a new patient, you could have a decision tree automatically multiply the length of the physical by 3 times to allow the provider enough time to gather any required new patient paperwork.
  - Here is an example of how this option works: Say the visit added by the decision tree is 15 minutes. When scheduled with Dr. Roberts who has a visit type modifier to add 5 minutes for that visit type, the new calculated length is 20 minutes. If you have an Add Visit node that multiplies the visit by 3, the final length for the visit is 60 minutes.

For advanced visit types, select the **Replace all original providers** check box to quickly replace all providers and subgroups in a pool with a list of providers and subgroups you specify in the node.

For appointment entry, replace the visit type the scheduler originally entered in Book It with the new visit.
For appointment entry, don't launch the decision tree or questionnaire that is linked to the new visit when this decision tree is applied.
For appointment entry and request entry, include instructions to tell schedulers what they should do next and how they should communicate the decision or next steps to the patient.

#### Decision Tree

*Applies to all types of decision trees.*

Creates a node for using another decision tree within the current decision tree. This is called nesting decision trees. You might nest a decision tree if you have common questions that apply to multiple scenarios and you don't want to rebuild the logic multiple times. You can also use nested decision trees to return values or scores that you can use to drive actions in the parent decision tree.

#### Display Instructions

*Applies to all types of decision trees.*

Creates a node for showing instructions to the user. These instructions appear on the screen, but the user doesn't need to respond to them. The user clicks a **Continue** button to proceed to the next node in the decision tree.

For patient self-triage decision trees, you can choose to show different instructions to patients and providers. Enter the patient instructions in the **Instructions** field and the provider instructions in the **Provider Instructions** field. If you leave the **Provider Instructions** field blank, providers see the same instructions that patients see.

#### Evaluate Score

*Applies to all types of decision trees.*

Creates a node for evaluating the total score that has been calculated from Question, Questionnaire, and Rule nodes earlier in the decision tree. Use this node when you want to branch the logic of a decision tree based on a score.

For more information about using scores in decision trees, refer to the Use the Results of a Nested Decision Tree to Drive Other Actions topic.

#### Modify Visit

*Applies only to appointment entry and request entry decision trees. Note that this node type is not supported in new provider scheduling in versions prior to February 2022 or open scheduling.*

For appointment entry, this node modifies the visit that the scheduler originally entered in Book It when she applies the decision tree. For request entry, this node modifies the original visit in the Visit section of the Appointment Request activity. You can optionally choose to:

For appointment entry, change the length of the visit:
- **Add or subtract time.** Enter the number of minutes in multiples of 5.
- **Replace.** Enter any amount of time as the final visit length. Overrules every other change option.
- **Add Slot Lengths** (starting in November 2023). Enter the number of default slot lengths, between 1-100 slots. A provider's default slot length is set in **Slot Length (mins)** field on the settings tab of the provider's template or by following the path Epic button > Admin > Schedule Admin > Templates > Rel Date/Defaults.
  - This option is especially useful when scheduling visits that you need to extend, but your providers each have different slot lengths on their templates.
  - Your providers might have slots lengths on their template that do not match their default slot length, so use caution when using this option with those providers. A scheduler could end up splitting the slots on a provider's scheduler if the extended visit length does not match the slots on the provider's schedule, in which case the other half of the split slot can't be scheduled.
  - Here is an example of how this option works: Dr. Roberts has a Default Slot Length of 10 minutes and Dr. Chavez has a Default Slot Length of 15 minutes. The visit being modified by the decision tree is 30 minutes. If you use a Modify Visit node that adds 2 slot lengths, when scheduled with Dr. Roberts the final length of the visit is now 50 minutes and when scheduled with Dr. Chavez the final length of the visit is 60 minutes.
- **Multiply** (starting in November 2023). Enter the number of times to multiply the length, between 2-10 times its calculated length. The calculated length of a visit is affected by Visit Type Modifiers.
  - This option is useful if you need to extend the length of a visit in large increments depending on patient rules. For example, if you have a patient coming in for an annual physical, but they are also a new patient, you could have a decision tree automatically multiply the length of the physical by 3 times to allow the provider enough time to gather any required new patient paperwork.
  - Here is an example of how this option works: Say the visit being modified by the decision tree is 15 minutes. When scheduled with Dr. Roberts who has a visit type modifier to add 5 minutes for that visit type, the new calculated length is 20 minutes. If you have a Modify Visit node that multiplies the visit by 3, the final length for the visit is 60 minutes.

For advanced visit types, select the **Replace all original providers** check box to quickly replace all providers and subgroups in a pool with a list of providers and subgroups you specify in the node.

Don't launch the decision tree or questionnaire that is linked to the modified visit when this decision tree is applied.
Include instructions to tell schedulers what they should do next and how they should communicate the decision or next steps to the patient.

#### Question

*Applies to all types of decision trees.*

Creates a node for asking the user a question. You can ask questions that are multiple choice or free text. You can also include instructions with the question.

For patient self-triage decision trees, you can choose to show different instructions to patients and providers. Enter the patient instructions in the **Instructions** field and the provider instructions in the **Provider Instructions** field. If you leave the **Provider Instructions** field blank, providers see the same instructions that patients see.

You can use the Scoring section to assign scores to different answers to the question. For more information about using scores in decision trees, refer to the Use the Results of a Nested Decision Tree to Drive Other Actions topic.

For more information on building question records, refer to the Form Questions and Questionnaire Setup and Support Guide.

#### Questionnaire

*Applies to all types of decision trees.*

Creates a node for showing a questionnaire to the user. The questionnaire appears as it normally would when used outside of a decision tree.

You can use the Scoring section to assign scores to different rules in the questionnaire. Create the rules using a **5001-Questionnaire** context for all decision trees except patient self-triage decision trees. For patient self-triage decision trees, create the rules using a **32002-MyChart Patient Self-Triage** context.

To use the scoring section of a questionnaire node, you need to create a Questionnaire context rule that uses the questionnaire utilized in the node.

If you are building a patient self-triage decision tree, only questionnaires of type **100-Patient Entered Questionnaires** are allowed, and PROMIS CAT questionnaires are not supported.

For more information on building questionnaire records, refer to the Form Questions and Questionnaire Setup and Support Guide.

#### Replace Visit

*Applies only to Book Anywhere decision trees.*

Replaces the visit type sent from the external location with the visit type used by your organization.

You can change the length of the visit:
- **Add or subtract time.** Enter the number of minutes in multiples of 5.
- **Replace.** Enter any amount of time as the final visit length. Overrules every other change option. Open decision tree **1170000012-ES Pulmonary Function Test (PFT) Duration** tree in the Foundation System to see an example of the Replace option.
- **Add Slot Lengths** (starting in November 2023). Enter the number of default slot lengths, between 1-100 slots. A provider's default slot length is set in **Slot Length (mins)** field on the settings tab of the provider's template or by following the path Epic button > Admin > Schedule Admin > Templates > Rel Date/Defaults.
  - This option is especially useful when scheduling visits that you need to extend, but your providers each have different slot lengths on their templates.
  - Your providers might have slots lengths on their template that do not match their default slot length, so use caution when using this option with those providers. A scheduler could end up splitting the slots on a provider's scheduler if the extended visit length does not match the slots on the provider's schedule, in which case the other half of the split slot can't be scheduled.
  - Here is an example of how this option works: Dr. Roberts has a Default Slot Length of 10 minutes and Dr. Chavez has a Default Slot Length of 15 minutes. The visit added by the decision tree is 30 minutes. If you use an Replace Visit node that adds 2 slot lengths, when scheduled with Dr. Roberts the final length of the visit added is now 50 minutes and when scheduled with Dr. Chavez the final length of the visit added is 60 minutes.
- **Multiply** (starting in November 2023). Enter the number of times to multiply the length, between 2-10 times its calculated length. The calculated length of a visit is affected by Visit Type Modifiers.
  - This option is useful if you need to extend the length of a visit in large increments depending on patient rules. For example, if you have a patient coming in for an annual physical, but they are also a new patient, you could have a decision tree automatically multiply the length of the physical by 3 times to allow the provider enough time to gather any required new patient paperwork.
  - Here is an example of how this option works: Say the visit added by the decision tree is 15 minutes. When scheduled with Dr. Roberts who has a visit type modifier to add 5 minutes for that visit type, the new calculated length is 20 minutes. If you have an Replace Visit node that multiplies the visit by 3, the final length for the visit is 60 minutes.

For advanced visit types, select the **Replace all original providers** check box to quickly replace all providers and subgroups in a pool with a list of providers and subgroups you specify in the node.

You can also specify instructions to be passed back to the scheduler.

#### Rule

*Applies to all types of decision trees.*

Creates a node for adding a connection that evaluates a rule to determine how to proceed in the decision tree. For example, you might branch a decision tree based on the patient's age.

- For appointment entry decision trees, choose from **5003-Appointment Entry Begin** context rules. If you're configuring a decision tree for MyChart open scheduling, make sure to avoid rules that evaluate patient data, since no authenticated patient record exists yet.
- For Book Anywhere decision trees, choose from **5003-Appointment Entry Begin** and **5060-Book Anywhere** context rules.
- For financial and request entry decision trees, choose from **5008-Appointment Request** context rules.
- For patient self-triage decision trees, choose from **32002-MyChart Patient Self-Triage** context rules.

You specify the rule to use in the connection you draw from the rule node to the next node in your tree. Refer to the Add Connections Between Nodes topic for more information.

**Starting in May 2025**

Using the Rule Tester, you can test rules that use context **5003-Appointment Entry Begin** such as those used in appointment entry decision trees. This is a great way to troubleshoot rule logic and save time by not needing to fully run a decision tree in a scheduling workflow.

A few things to keep in mind when using the Rule Tester for Appointment Entry Begin rules:

- The system cannot hide or filter fields based on responses to other fields in the Rule Tester. This means it's possible to pick "incompatible" records. For example, you can select a visit type, then select an order that has a completely different Visit Type attached to it. We suggest filling out as few fields as possible in the Rule Tester to test all the conditions in your rule. This ensures you don't run into any issues with incompatible records and makes it easier to verify individual conditions are working properly.
- All multi-select fields are evaluated with the records in that field, in addition to records in other fields in the Rule Tester. For example, if you select Patient A in the Patient field, but select one of Patient B's encounters in a different field, the rule is evaluated for both Patient A and B.

#### Schedule Appointment Request

*Applies only to patient self-triage decision trees.*

Use this node after an Add Appointment Request node to allow patients to schedule a visit if it meets certain criteria. Create rules in the context **5008-Appointment Request** to connect the nodes. For example, you might create a rule that checks the status of the appointment request after it's been created. If the appointment request is at a status where it's ready to be scheduled, you might link it to a Schedule Appointment Request node.

#### Select Treatment/Therapy Plan

**Starting in February 2024**

*November 2023 by SU E10703445, C10703445-HSWeb, E10703455, E10703456*

*August 2023 by SU E10608089, C10608089-HSWeb, E10608099, E10608100*

*May 2023 by SU E10514309, C10514309-HSWeb, E10514324, E10514325*

*February 2023 by SU E10417133, C10417133-HSWeb, E10417137, E10417138*

*Applies only to appointment entry decision trees.*

You can use the Select Treatment/Therapy Plan node to make it easy for scheduling staff to schedule the right visit length for a patient's infusion if your organization meets either of the following conditions:

- You don't generate appointment requests for infusions from treatment or therapy plans.
- You generate appointment requests for infusions from treatment or therapy plans, but there are occasions when schedulers don't use the appointment requests for scheduling. For example, a scheduler might not use an appointment request if the clinician hasn't signed orders yet or is updating the patient's treatment or therapy plan.

The Select Treatment/Therapy Plan node prompts schedulers to select the treatment plan or therapy plan for which they are scheduling a visit. If the system can determine a length for the visit, that length appears automatically in the Infusion appointment length field in the decision tree. Schedulers can override the calculated visit length or specify a length if one wasn't calculated. Schedulers can expand the decision tree sidebar to see details about the selected treatment plan or therapy plan so they can be confident they selected the right one. By linking the appointment to the patient's treatment plan or therapy plan, the system is also able to link any referrals for the treatment plan or therapy plan to the patient's appointment.

The system doesn't calculate visit lengths for therapy plans, so schedulers always need to enter a length for therapy plan visits. The system can automatically determine a length for a treatment plan visit if either of the following is true:

- You've configured the infusion duration table, as described in the Build the Infusion Duration Table topic.
- You're allowing automatic visit length calculations using medication offsets and durations, as described in the Calculate Infusion Duration Using Medication Offsets and Durations topic.

Starting in February 2025 and in November 2024 with special updates E11200791, E11200790, and E11200695; and in August 2024 with special updates E11106471, E11160470, and E1116408, decision tree builders can choose to hide the length question from schedulers when a tree is run. To hide the length question, select the **Hide infusion appointment length field (I LQL 1260)** checkbox in the node. When the length question is hidden from schedulers, the appointment length is based on the default length of the visit type with any modifications supplied by the decision tree.

If a patient doesn't have a treatment plan or therapy plan, the node shows a message to the scheduler indicating that no plans were found. Schedulers can continue through the decision tree and schedule a visit, but they won't be able to select a plan to link to the appointment.

#### Set Output Value

*Applies to all types of decision trees.*

Creates a node that sets an output value when used with a decision tree that outputs custom values. For more information about using output values in decision trees, refer to the Use the Results of a Nested Decision Tree to Drive Other Actions topic.

#### Set Telehealth Mode

**Starting in May 2023**

*Applies only to appointment entry and request entry decision trees.*

Sets the telehealth mode for an appointment. You can choose any telehealth mode that's been set up in your system.

Starting in August 2023, you can also automatically set patient arrival locations based on the telehealth mode. To configure this behavior, enter the arrival location in the **Arrival Location** field. If you leave this field blank, the system uses the default arrival locations associated with the telehealth mode.

### Create SmartText Instructions for Decision Tree Nodes

Some nodes support showing instructions to schedulers or patients. You can write the instructions directly in the node or create reusable SmartText records for the instructions. We recommend using SmartTexts whenever possible to simplify maintenance.

Create SmartText instructions for:
- **Appointment entry decision trees** in the **Appointment Entry Tree Instructions Editor** (search: Appointment Entry Tree Instructions)
- **Financial and request entry decision trees** in the **Request Entry Tree Instructions Editor** (search: Request Entry Tree Instructions)
- **Patient self-triage decision trees** in the **Patient Self-Triage Tree Instructions Editor** (search: Patient Self-Triage Tree Instructions)

### Map Indications to Request Entry Decision Trees

If you want a request entry decision tree to appear as a suggested decision tree in the Decision Tree Search section of the Appointment Request activity when a patient has certain diagnoses entered in the Indications section, you can map diagnoses to the decision tree.

1. In Hyperspace, open **Cadence System Definitions** and select **Scheduling > Decision Trees**.
2. In the **Request Entry Decision Tree Indication Mapping** table, enter the decision tree in the **Decision Tree (I SDF 12730)** column and the diagnoses in the **Indication (I SDF 12731)** column.

### Define the Financial Decision Tree for Your Organization

If you want to perform financial screening for patients in appointment requests before you schedule visits for them, you can set up a financial decision tree and make it available to your schedulers. For more information about financial screening, refer to the Perform Financial Screening in Appointment Requests topic.

To make the tree available to schedulers:

1. In Hyperspace, open **Cadence System Definitions** and select **Scheduling > Decision Trees**.
2. In the **Financial Decision Tree (I SDF 12710)** field, enter your financial decision tree.

### Define the Patient Self-Triage Decision Trees for Your Organization

To make the trees available to MyChart patients:

1. From the **MyChart System Manager Menu**, select either:
   - For **Patient Access System Definitions**, select **Care Companion & Pat-Entered Data** (named Patient Entered Data in November 2024 and earlier versions).
   - For **patient profiles**, select **Patient Profile Settings** and open your patient profile.

2. Go to the **Self-Triage Settings** screen and set the following items:
   - In the **Store partially completed decision trees for (I WDF 13520)** field, enter a number of hours after which partially completed self-triage decision trees are no longer available to the patient. Partially completed decision trees, or decision trees that the patient began but didn't receive triage recommendations from, older than the number of hours specified here are removed from the patient's MyChart during the next login. The default is 48 hours. Starting in May 2023, partially completed trees older than the number of hours specified here are marked as abandoned but are not deleted, which allows for reporting on self-triage abandonment. In February 2023 and earlier, qualifying decision tree data is purged from the database.
   - Starting in February 2024, in the **Store actionable decision trees for (I WDF 13525)** field, enter a number of hours after which actionable self-triage decision trees are no longer available to the patient. Actionable decision trees, or decision trees that the patient began and received triage recommendations from, older than the number of hours specified here are removed from the patient's MyChart during the next login. The actionable decision trees are marked as abandoned but are not deleted, which allows for reporting on self-triage abandonment. The default is 48 hours. If you have a case where you want the triage recommendations to always be available to the patient, edit that symptom's decision tree build by selecting the **Prevent expiration if tree has incomplete recommendations (I LQF 700)** checkbox. Starting in May 2025, February 2025 with special updates C11303610, E11303646, E11303647, and E11303649, you can set the number of hours that the actionable recommendations remain available at the decision tree level (I LQF 705).
   - In the **Default Provider (I WDF 13530)** field, enter your default provider. This provider is listed as the ordering and signing provider if orders are signed automatically, as well as the default for encounter creation and order and results routing. The default provider must be an active provider record, an orders-authorizing provider (I SER 8220), and must be linked to a user (EMP) record.
   - In the **Default Department (I WDF 13540)** field, enter your default department for encounter creation and order routing purposes. To learn how this affects routing in more detail for the Add Order node, refer to the Add Order topic.

3. Go to the **Self-Triage Decision trees** screen (in May 2022 and earlier, stay on the Self-Triage Settings screen and use the Available Decision Trees table) and add your decision trees and filter rules.
   - In the **Decision Tree (I WDF 13500)** column, enter your decision tree.
   - If you want to use a filtering rule, create a filter rule with a context of **32500-Patient (No Default Contact)**, as described in the Create or Edit a Rule topic. Then enter the filter rule in the **Filtering Rule (I WDF 13510)** column. If the rule evaluates to true, the decision tree is available to the patient.
   - Starting in November 2022, in the **Deep Link Only (I WDF 13515)** column, enter **1-Yes** to make the decision tree available only for deep linking. This also hides the decision tree on the Symptom Checker landing page. If this field is left blank, the default value is **0-No** and the decision tree is available on the Symptom Checker landing page.

4. If you have turned on self-triage for patients without a MyChart account (available starting in August 2023 and in May 2023 with special update E10501418), go to the **Self-Triage for All Decision Trees** screen and add your decision trees.
   a. In the **Decision Tree (I WDF 13600)** column, enter the self-triage decision trees that should be available to new patients for self-triage. Each decision tree acts as an individual point of entry for the patient to initiate a self-triage workflow without a MyChart account.
   b. In the **Deep Link Only (I WDF 13615)** column, enter **1-Yes** to mark a decision tree for deep linking only which means the decision tree does not show up on the Symptom Checker page for patients without a MyChart account. If left blank, this field is set to **0-No** and new patients can see this decision tree on the self-triage for all landing page. Refer to the Link Patients Directly to Self-Triage Decision Trees topic for more information about linking directly to self-triage decision trees.

5. Starting in November 2024, go to the **Self-Triage Secure Link Settings** screen and add your decision trees in the **Decision Tree (I WDF 13490)** column. These self-triage decision trees are then available to send to patients from the Send Self-Triage Tree activity in Appointment Desk. Refer to the Send Self-Triage Decision Trees from Appointment Desk topic for more information about sending links to trees from Appointment Desk.

#### Configure Affiliate-Specific Departments for Self-Triage Encounters

You can associate self-triage encounters created at affiliate sites with affiliate-specific departments by configuring the Affiliate Settings table in Patient Access System Definitions:

1. From the **MyChart System Manager Menu**, select **Login and Access Configuration** and access the **Affiliate Settings** screen.
2. In the **Affiliate Site Name (I WDF 2570)** field, enter the Site ID for the affiliate.
3. In the **Affiliate Default Department (I WDF 2575)** field, enter the department that should be used for self-triage encounters and orders. If you set the **Default Department (I EAF 32702)** field in the location or service area level, that department is used instead for self-triage encounters and orders.

#### Configure Decision Trees in the Facility Structure

**Starting in May 2023**

You can configure decision trees in your facility structure to allow affiliate organizations to use different self-triage decision trees. For example, you can use a different decision tree for fever that has different questions and nodes in your affiliate's Service Area Profile to account for children at an affiliate children's hospital.

##### Prerequisites

To define self-triage decision trees for affiliate site, you need to complete additional setup for affiliates:

- Define the site IDs and URLs for your affiliate organizations on the **MyChart Access URL Configuration** screen as described in the Define URLs for Affiliates topic.
- Configure the **Affiliate Settings** table as described in the Configure Affiliate-Specific Departments for Self-Triage Encounters section in the Define the Patient Self-Triage Decision Trees for Your Organization topic.

To make the trees available to MyChart patients:

1. In **MyChart System Manager Menu**, select **Master File Edit**.
2. Select either **Facility**, **Service Area Profile**, or **Location** depending on what facility structure level you want to configure and open your record.
3. Go to the **Self-Triage Settings** screen.
4. In the **Store partially completed decision trees for (I EAF 32700)** field, enter the number of hours after which partially completed self-triage decision trees are no longer available to the patient. Partially completed decision trees, or decision trees that the patient began but didn't receive triage recommendations from, older than the number of hours specified here are removed from the patient's MyChart during the next login. The default is 48 hours. Starting in May 2023, partially completed trees older than the number of hours specified here are marked as abandoned but are not deleted, which allows for reporting on self-triage abandonment. In February 2023 and earlier, qualifying decision tree data is purged from the database.
5. Starting in February 2024, in the **Store actionable decision trees for (I EAF 32705)** field, enter a number of hours after which actionable self-triage decision trees are no longer available to the patient. Actionable decision trees, or decision trees that the patient began and received triage recommendations from, older than the number of hours specified here are removed from the patient's MyChart during the next login. The actionable decision trees are marked as abandoned but are not deleted, which allows for reporting on self-triage abandonment. The default is 48 hours. If you have a case where you want the triage recommendations to always be available to the patient, edit the symptom's decision tree build by selecting the **Prevent expiration if tree has incomplete recommendations (I LQF 700)** checkbox. Starting in May 2025, February 2025 with special updates C11303610, E11303646, E11303647, and E11303649, you can set the number of hours that the actionable recommendations remain available at the decision tree level (I LQF 705).
6. In the **Default Provider (I EAF 32701)** field, enter your default provider. This provider is listed as the ordering and signing provider if orders are signed automatically, as well as the default for encounter creation and order and results routing. The default provider must be linked to a user (EMP) record.
7. In the **Default Department (I EAF 32702)** field, enter the same department you entered in **Affiliate Default Department (I WDF 2575)** field. If you want to use a different department for encounter creation and order routing purposes at your Location or Service Area level rather than the affiliate-level department, you can enter a different department here.
8. Go to the **Self-Triage Decision Trees** screen and add your decision trees and filter rules.
   - In the **Decision Tree (I EAF 32703)** column, enter your decision tree.
   - If you want to use a filtering rule, create a filter rule with a context of **32500-Patient (No Default Contact)**, as described in the Create or Edit a Rule topic. Then enter the filter rule in the **Filtering Rule (I EAF 32704)** column. If the rule evaluates to true, the decision tree is available to the patient.

### Make an Appointment Entry Decision Tree Available at the Visit Type or Panel Level

You can link an appointment entry decision tree directly to a visit type or a panel so that the decision tree launches when schedulers select the visit type or any visit types in the panel.

#### Link a Decision Tree to a Visit Type

1. In Hyperspace, open the **Visit Type Editor** (search: Visit Type) and search for your visit type.
2. Go to the **Tree & Questionnaire** form.
3. In the **Decision Tree (I VTY 21900)** field, enter your decision tree.
4. If you want the decision tree to run silently in the background instead of showing questions to the scheduler, select the **Silent Tree (I VTY 21901)** check box. The decision tree still performs the actions you've configured, such as changing the visit type, but schedulers don't see any questions or instructions from the tree.

#### Link a Decision Tree to a Panel

1. In Hyperspace, open the **Panel Editor** (search: Panel) and search for your panel.
2. In the **Decision Tree (I PNL 2800)** field, enter your decision tree.
3. If you want the decision tree to run silently in the background instead of showing questions to the scheduler, select the **Silent Tree (I PNL 2801)** check box. The decision tree still performs the actions you've configured, such as changing the visit type, but schedulers don't see any questions or instructions from the tree.

### Define the Book Anywhere Decision Tree for Your Organization

If you want to process requests from external locations to schedule appointments at your organization, you can set up a Book Anywhere decision tree and make it available to your schedulers. For more information about Book Anywhere, refer to the Book Anywhere Setup and Support Guide.

To make the tree available to schedulers:

1. In Hyperspace, open **Cadence System Definitions** and select **Scheduling > Decision Trees**.
2. In the **Book Anywhere Decision Tree (I SDF 12720)** field, enter your Book Anywhere decision tree.

### Show the Results of an Appointment Entry Decision Tree to Schedulers

When schedulers run an appointment entry decision tree, you can choose to show them a summary of the results of the decision tree. For example, you might show them which visit type the decision tree recommended or which provider pool was suggested.

To show the results to schedulers:

1. In Hyperspace, open **Cadence System Definitions** and select **Scheduling > Decision Trees**.
2. Select the **Show decision tree results to schedulers (I SDF 12740)** check box.

### Show the Results of Scheduling Decision Trees to Clinicians

When providers view appointments that were scheduled using decision trees, you can show them information about the decision trees that were used. This can help providers understand why certain scheduling decisions were made.

To show the results to clinicians:

1. In Hyperspace, open **Cadence System Definitions** and select **Scheduling > Decision Trees**.
2. Select the **Show decision tree results to providers (I SDF 12741)** check box.

### Show the Results of a Patient Self-Triage Decision Tree to Providers

When patients complete self-triage decision trees, you can show the results to providers in the patient's chart. This can help providers understand what symptoms the patient reported and what recommendations they received.

To show the results to providers:

1. From the **MyChart System Manager Menu**, select **Care Companion & Pat-Entered Data** (named Patient Entered Data in November 2024 and earlier versions).
2. Go to the **Self-Triage Settings** screen.
3. Select the **Show self-triage results to providers (I WDF 13550)** check box.

## Decision Trees Setup: Bells & Whistles

This section covers optional configuration that can enhance the decision tree experience for your organization.

### Make an Appointment Entry Decision Tree Available at the Department or System Level

You can make an appointment entry decision tree available at the department or system level so that it applies to multiple visit types without having to link it to each visit type individually.

#### Make a Decision Tree Available at the Department Level

1. In Hyperspace, open the **Department Editor** (search: Department) and search for your department.
2. Go to the **Scheduling** form.
3. In the **Decision Tree (I DEP 15200)** field, enter your decision tree.
4. If you want the decision tree to run silently in the background instead of showing questions to the scheduler, select the **Silent Tree (I DEP 15201)** check box.

#### Make a Decision Tree Available at the System Level

1. In Hyperspace, open **Cadence System Definitions** and select **Scheduling > Decision Trees**.
2. In the **System-Wide Decision Tree (I SDF 12700)** field, enter your decision tree.
3. If you want the decision tree to run silently in the background instead of showing questions to the scheduler, select the **Silent Tree (I SDF 12701)** check box.

### Limit How Many Times a Patient Can Start a Self-Triage Decision Tree in 24 Hours

You can limit how many times a patient can start the same self-triage decision tree in a 24-hour period to prevent overuse of the system.

1. From the **MyChart System Manager Menu**, select **Care Companion & Pat-Entered Data** (named Patient Entered Data in November 2024 and earlier versions).
2. Go to the **Self-Triage Settings** screen.
3. In the **Max decision trees per patient per day (I WDF 13560)** field, enter the maximum number of times a patient can start any self-triage decision tree in a 24-hour period.

### Show Risk Score Information in Decision Trees

You can show risk score information in decision trees to help schedulers understand the urgency of scheduling an appointment for a patient.

To show risk score information:

1. In Hyperspace, open **Cadence System Definitions** and select **Scheduling > Decision Trees**.
2. Select the **Show risk scores in decision trees (I SDF 12750)** check box.

### Show Related Orders and Appointments Requests in Decision Trees

You can show related orders and appointment requests in decision trees to help schedulers understand the full picture of a patient's care needs.

To show related information:

1. In Hyperspace, open **Cadence System Definitions** and select **Scheduling > Decision Trees**.
2. Select the **Show related orders and requests (I SDF 12760)** check box.

### Use Rules to Evaluate How Many Orders Are Linked to an Appointment

You can create rules that evaluate how many orders are linked to an appointment and use those rules in decision trees to determine scheduling actions.

Create rules using the **5003-Appointment Entry Begin** context and use property **98300-Linked Orders Count** to evaluate the number of orders.

### Use the Results of a Nested Decision Tree to Drive Other Actions

You can use nested decision trees to capture information and then use the results of those nested trees to drive actions in the parent tree. This section covers how to use custom output values and scores in decision trees.

When you embed one decision tree within another, the child decision tree can pass information back to the parent decision tree in two ways:

- **Use custom values** when you want to assign a value that doesn't come from a question or rule.
- **Use scores** when you want to assign a value based on the answer to a question or based on how the system evaluates rules, either from a visit type questionnaire or a rule node.

When you've set up decision trees to save a custom value or calculate a score, and that value or score is meaningful for a scheduler to help them understand why an appointment was scheduled a certain way, you can make it visible to them in scheduling workqueues and reports.

For example, decision tree **1170000013-Headache Scoring** is nested in request entry decision tree **1170000003-EHS Neurology Appointment Request** in the Foundation System. The child decision tree asks questions about the severity, frequency, and triggers of a patient's headaches and applies scores based on the responses. If the total score is at least 10, the decision tree results include an Urgent tag that allows the scheduler to schedule into slots with an Urgent block so the patient can be seen sooner. To see how these scheduling trees are set up, log in to the Foundation Hosted environment as your organization's Cadence analyst (ESADM) and open them in the Request Entry Decision Tree activity (search: Request Entry Decision Tree).

The steps below assume you've already created a decision tree and know how to add nodes and draw connections.

#### Define and Use Custom Output Values in Decision Trees

To use custom output values, you need to define those values and set them in the logic of a child decision tree and then set up a parent decision tree to evaluate the output values that are set by the child decision tree.

##### Set Up a Child Decision Tree to Output Custom Values

1. In the decision tree editor, select the **Output Value** tab.
2. Select **Custom Value**.
3. Add the custom values that the decision tree can output, or copy values from another decision tree.
4. Select a default value to use if a decision tree branch ends without specifying a value.
5. Select the **Decision Tree** tab.
6. Add **Set Output Value** nodes as end nodes in the tree logic to set the custom values you created.

##### Set Up a Parent Decision Tree to Use Custom Values Set by a Child Decision Tree

1. Use a **Decision Tree** node to add a child decision tree. The Node Details show the output type and possible output values.
2. When you draw connections from a Decision Tree node to other nodes, select the **Embedded Tree Output** connection type to use output values from the child decision tree to drive logic in the parent tree.

#### Define and Use Scores in Decision Trees

To use scores, you need to set them in the logic of a child decision tree and then set up a parent decision tree to evaluate the scores that are set by the child decision tree. You can also evaluate a score within a child or parent decision tree.

##### Set Up a Child Decision Tree to Output Scores

1. In the decision tree editor, select the **Output Value** tab.
2. Select **Score**.
3. Select the **Decision Tree** tab.
4. Select or add a **Question**, **Questionnaire**, or **Rule** node.
5. Use the **Scoring** section to define scores for each answer for a question, each rule in a questionnaire, or the Appointment Entry Begin rules you specify.

> **Tip:** Hover the mouse pointer over a node to view a tooltip with score details for the node.

##### Set Up a Parent Decision Tree to Use Scores Set by a Child Decision Tree

1. Use a **Decision Tree** node to add a child decision tree. The Node Details show the output type.
2. When you draw connections from a Decision Tree node to other nodes, select the **Embedded Tree Output** connection type to use scores from the child decision tree to drive logic in the parent tree.

##### Evaluate Scores in the Same Tree Where They Are Set

To evaluate a score within a child or parent decision tree, add an **Evaluate Score** node after the Question, Questionnaire, and Rule nodes that set scores in the tree. In the connections you draw from the Evaluate Score node, select the **Score** type and enter the score value to evaluate.

#### Show Decision Tree Output Values and Scores to Users

If the custom values and scores saved by decision trees are meaningful to users to help them understand why an appointment was scheduled a certain way, you can show them in columns in patient workqueues; schedule orders/appointment request workqueues; Cadence reports, such as Appointment Desk tabs and the Department Appointments report; and appointment-based Reporting Workbench reports.

##### Make a Decision Tree's Output Values or Scores Visible to Users

In the decision tree editor, on the **Basic Information** tab, select the **Allow this decision tree's score/output to be shown to end users (I LQF 690)** check box.

##### Add Decision Tree Output Value and Score Columns to Workqueues

There are two properties you can use as columns in schedule orders/appointment request workqueues and patient workqueues to show users the output value or score from the decision trees that are associated with a request or appointment:

- **98267-Appt Request - Tree Score and Custom Output.** Shows the output value or score from the request entry decision trees associated with a request in a schedule orders/appointment request workqueue.
- **98268-Decision Tree Score and Custom Output Value.** Shows the output value or score from the appointment entry and request entry decision trees associated with an appointment in a patient workqueue.

As released, these properties show scores and output values from all decision trees that have been applied to a request or appointment along with the decision tree names. You can customize copies of these properties to show scores and output values from specific decision trees and also hide the decision tree names.

1. In Hyperspace, open the **Property Editor** and select the appropriate context for the property you want to customize:
   - For property 98267, select the **Appointment Request** or **Order** context.
   - For property 98268, select the **Patient** context.
2. Expand the advanced search options and search for the property you want to copy by record ID.
3. Select the property and click **Copy**. Starting in May 2024, the General, Lookup, and Restrictions tabs have been converted into sections.
4. Go to the **Lookup** tab/section for your copied property and customize the parameters as needed:
   - **Decision Tree IDs.** Enter the ID numbers of the decision trees you want to show scores and output values for. As released, this parameter is blank, and scores and output values appear for all decision trees that have been applied to the appointment.
   - **Hide Decision Tree Name?** Enter **Yes** to hide the names of decision trees in the column. As released, this parameter is blank, and decision tree names appear in the column.

Refer to the Define Workqueue Columns and Sort Order topic for information about adding columns to workqueues.

##### Add Decision Tree Output Value and Score Columns to Reports

There are two columns that you can add to Cadence and Reporting Workbench reports to show users the output value or score from the decision trees that are associated with an appointment:

- **1949-Decision Tree Score and Custom Value Output.** Shows the output value or score from the appointment entry and request entry decision trees associated with an appointment.
- **1967-Appt Request Score and Custom Value Output.** Shows the output value or score from the request entry decision tree associated with an appointment.

As released, these columns show scores and output values from all decision trees that have been applied to an appointment along with the decision tree names. You can customize copies of these columns to show scores and output values from specific decision trees and also hide the decision tree names.

1. In Chronicles, access the **Extension (LPP)** master file.
2. Duplicate one of the following extensions, depending on which column you're customizing:
   - For column 1949, duplicate extension **42416-ES PAF Decision Tree Scores and Custom Value Outputs**.
   - For column 1967, duplicate extension **42418-ES PAF Request Tree Scores and Custom Value Outputs**.
3. Customize the parameters as needed:
   - **Decision Tree IDs.** Enter the ID numbers of the decision trees you want to show scores and output values for. As released, this parameter is set to null (""), and scores and output values appear for all decision trees that have been applied to the appointment.
   - **Hide Decision Tree Name?** Enter **Yes** to hide the names of decision trees in the column. As released, this parameter is set to null (""), and decision tree names appear in the column.
4. In Hyperspace, open the **Column Editor** (search: Column Editor).
5. Select the **Create New Column** tab and duplicate column 1949 or 1967.
6. On the **General** tab, update the **Extension (I CNM 1800)** field to reference your duplicated extension.

Refer to the Build a Report topic for information about adding columns to reports.

### Use Nested Decision Trees to Give Patients Options in Self-Triage

You can use nested decision trees in patient self-triage to give patients options about their care. For example, you might have a parent decision tree that asks about a patient's symptoms, and then based on their answers, presents them with a child decision tree that gives them options for next steps.

### Associate Self-Triage Decision Tree Orders With a Department

You can associate orders created by self-triage decision trees with a specific department to ensure they are routed to the correct providers.

1. In the **Patient Self-Triage Decision Tree** editor, go to the **Basic Information** tab.
2. In the **Associated Department (I LQF 32500)** field, enter the department that should be associated with orders created by this decision tree.

### Let Patients Request an Appointment from Self-Triage

You can configure self-triage decision trees to allow patients to request an appointment directly from the decision tree results.

Use the **Add Appointment Request** node in your self-triage decision trees to allow patients to create appointment requests that are sent to your organization's scheduling staff.

### Bundle Orders with Appointments That Patients Can Schedule Together

You can bundle orders with appointments so that when patients schedule certain appointments through self-triage, related orders are automatically created.

Use the **Add Order** node in conjunction with the **Add Appointment Request** or **Schedule Appointment Request** nodes to bundle orders with appointments.

### Send Self-Triage Decision Trees from Appointment Desk

**Starting in November 2024**

You can send links to self-triage decision trees directly to patients from the Appointment Desk. This allows schedulers to provide patients with specific self-triage tools relevant to their symptoms or conditions.

To configure this functionality:

1. Set up your self-triage decision trees in the **Self-Triage Secure Link Settings** as described in the Define the Patient Self-Triage Decision Trees for Your Organization topic.
2. Schedulers can then use the **Send Self-Triage Tree** activity in Appointment Desk to send secure links to patients.

### Define an Expected Path Through Appointment Entry Decision Trees

You can define an expected path through appointment entry decision trees to help with testing and validation of your decision tree logic.

1. In the **Appointment Entry Decision Tree** editor, go to the **Expected Path** tab.
2. Define the expected sequence of nodes that the decision tree should follow for typical scenarios.
3. Use this information to validate that your decision tree logic is working as expected during testing.

## Decision Trees Support: Ongoing Tasks

This section covers common tasks you'll need to perform to maintain and support your decision trees after they've been implemented.

### View a Decision Tree

To view an existing decision tree:

1. In Hyperspace, open the appropriate decision tree editor:
   - **Appointment Entry Decision Tree**
   - **Book Anywhere Decision Tree** 
   - **Financial Decision Tree**
   - **Request Entry Decision Tree**
   - **Patient Self-Triage Decision Tree**
2. Search for the decision tree by name or ID.
3. Select the **Decision Tree** tab to view the visual representation of the tree.

### Edit a Released Decision Tree

When you need to edit a decision tree that has already been released to production, you have several options:

1. **Create a new contact** if you want to make significant changes and test them before releasing.
2. **Edit the existing contact** if you need to make minor changes that can go live immediately.

> **Important:** Be cautious when editing released decision trees in production, as changes take effect immediately and can impact active scheduling workflows.

### Search Within a Decision Tree

You can search for specific text within a decision tree to quickly find nodes or connections that contain certain information.

1. In the decision tree editor, select the **Decision Tree** tab.
2. Use **Ctrl+F** to open the search function.
3. Enter the text you want to search for.
4. The system highlights nodes and connections that contain your search term.

The search function looks through all text in the decision tree, including node names, instructions, question text, and connection criteria. When you search, the system shows you the specific node and connection where that text appears. The system even searches within the node or connection to find things like a provider entered in the provider modification table of an Add Visit node.

### Copy and Paste Nodes and Connections

**Starting in November 2023**

When you need to create multiple nodes or sections that are the same or similar, use the copy and paste functionality to copy elements of one decision tree either elsewhere within the same tree, or into a different tree of the same type. You can do so using the toolbar buttons, the right-click options, or Ctrl+C and Ctrl+V.

### Copy a Decision Tree Contact to a New or Existing Contact

When you're working in the decision tree editor, you can choose to create a new contact. Click **Copy Contact** and choose one of the following options:

- **Copy to existing contact.** Allows you to overwrite an existing contact with the contents of another contact. This can be helpful when you're working on updating a decision tree but things get messy and you want to start over with a fresh copy of an existing contact.
- **Copy to new contact.** Allows you to copy the contents of an existing contact to a new contact.

### View the Decision Making Path for a Decision Tree

If you want to see how a decision tree evaluated a particular contact to reach its result, you can open the result in the **Decision Tree Tracer** (search: Decision Tree Tracer). Here, the decision making path for that result is highlighted and numbered, and clicking any node or connection in that path provides additional details about how connections were evaluated based on data from the contact. Note that decision trees of type **45-Book Anywhere Decision Tree** aren't available in this feature.

### Test Drive a Decision Tree

**Starting in May 2025**

If you need to test your Appointment Entry or Request Entry decision trees to validate that changes or build are behaving as expected, you can do so directly in the decision tree editor on the **Test Drive** tab.

For **Appointment Entry trees**, you'll need to enter a patient and visit type for the tree to use. Then you can decide whether to start the tree from visit type entry, from a request, in which case you need to enter an order record, or from a referral, in which case you need to enter a referral record. Simply click **Start Test** and the decision tree runs just like it would during actual scheduling, allowing you to quickly validate if the path and outcomes you expect to occur do actually occur. For silent trees, after you click the **Start Test** button, the Results section appears immediately since there are no questions to answer.

For **request entry trees**, the only required information needed to run a test is a request (ORD) record. You can optionally enter a patient if you want to filter the options in the request field.

### Mark a Decision Tree As Reviewed

If your organization has a process for regularly reviewing the content of your decision trees to make sure it is current, you can keep track of when the decision tree was last reviewed in Hyperspace. After a user has reviewed the decision tree, they click the **Mark as Reviewed** button on the **Basic Information** tab of the decision tree editor.

This information is stored in the following items:
- **Decision Tree - Last Reviewed - User (I LQF 605)**
- **Decision Tree - Last Reviewed - Date (I LQF 606)**

### View the Records That Are Linked to a Decision Tree

Select the **Linked Records** tab in the decision tree editor to view a list of records that reference the decision tree. Click a link to edit the record.

Use the **Rule Usage** report (search: Rule Usage) to see when a rule is being used in a node or connection in a decision tree.

### View the Audit Trail for Changes Made to a Decision Tree

Select the **Audit Trail** tab in the decision tree editor to view a list of all the changes made to the decision tree. The system records the following changes:

- **New Contact.** The user created a new contact for the decision tree.
- **Tree Structure.** The user made changes to the nodes or connections in the decision tree.
- **Released.** The user released the contact they were editing.

### Find Decision Tree Rules and Questionnaires That Contain Certain Question Records

If you modify order-specific question (LQL) records, like those described in the Use Certain Conditions to Determine How a Question Appears topic, and those questions are used to drive decision tree-based scheduling, you can use the **Question Usage in Rules** utility to quickly find all decision tree rules and questionnaires that use the question record. With this information, you can update the rules and questionnaires as necessary to reflect the changes to the order-specific questions, ensuring that your schedulers continue to receive the appropriate scheduling suggestions.

You can access the utility by going to **Cadence Text > Utility Menu > Question Usage in Rules**. You can specify one or multiple question records in the utility. The utility returns the rule records that contain the question record, and whether the rule is used in a questionnaire (LQF) record. Note that if the rule has a context of Questionnaire, it isn't included in the utility's results because those types of rules aren't used in decision trees.

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic. This item is a Commercial Item, as that term is defined at 48 C.F.R. Sec. 2.101. It contains trade secrets and commercial information that are confidential, privileged, and exempt from disclosure under the Freedom of Information Act and prohibited from disclosure under the Trade Secrets Act. After Visit Summary, ASAP, Aura, Beacon, Beaker, Beans, BedTime, Best Care Choices for My Patient, Bones, Break-the-Glass, Bugsy, Caboodle, Cadence, Canto, Care Everywhere, Charge Router, Cheers, Chronicles, Clarity, Cogito ergo sum, Cohort, Comfort, Community Connect, Compass Rose, Cosmos, Cosnome, Cupid, Discovery, Epic, EpicCare, EpicCare Link, Epicenter, EpicShare, EpicWeb, Epic Earth, Epic Nexus, Epic Research, Garden Plot, Grand Central, Haiku, Happy Together, Healthy Planet, Hello World, Hey Epic!, Hyperdrive, Hyperspace, Kaleidoscope, Kit, Limerick, Lucy, Lumens, MyChart, Nebula, OpTime, Phoenix, Powered by Epic, Prelude, Radar, Radiant, Resolute, Revenue Guardian, Rover, Share Everywhere, SmartForms, Sonnet, Stork, System Pulse, Tapestry, Trove, Welcome, Willow, Wisdom, With the Patient at Heart, and WorldWise are registered trademarks, trademarks, or service marks of Epic Systems Corporation in the United States of America and/or other countries. Other company, product, and service names referenced herein may be trademarks or service marks of their respective owners. Patents Notice: www.epic.com/patents.

**EpicUUID:** 73DD2CEF-9217-4068-BB6E-B73543FF0D49