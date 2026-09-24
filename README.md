# Hospital System — Patient Queue Management

## Problem Statement
- Implement the following system for a hospital.
- There are 20 different specializations (e.g. Children, Surgery, etc).
- For each specialization, there are only 5 available spots [queue].
- **Adding a patient:**
  - Read the requested specialization [1-20].
  - Read the patient's name and status (0 = regular, 1 = urgent).
  - If 5 patients already exist in that section, apologize and don't accept.
  - If the patient is regular, add to the end of the queue. Otherwise (urgent), add to the beginning.
- **Print patients** for the specializations that have waiting patients.
- **Doctor pickup a patient:**
  - Read the requested specialization. If no patients, inform the doctor.
  - Otherwise, ask the patient to go with the doctor and remove them from the queue.

## Overview
A console-based hospital queue system supporting 20 specializations, each with a maximum of 5 waiting patients. Patients are added with a priority status (regular / urgent), displayed, and picked up by doctors.

## Class: `Hostpital`

### `__init__`
Creates a dictionary `sections` mapping each specialization number (1–20) to an empty list, representing that section's patient queue.

### `addPatient(section, name, status)`
1. Validates the section number is within `[1, 20]`.
2. Checks if the section's queue already has 5 patients — if so, refuses and prints an apology.
3. Inserts the patient based on `status`:
   - `status == 0` (regular) -> added to the queue.
   - `status == 1` (urgent) -> added ahead of regular patients.

### `show_patients()`
Loops through all sections; for each section with at least one waiting patient, prints the section number and lists each patient's name with their status label ("regular"/"Urgent").

### `pickup_patient(section)`
1. If the section's queue is empty, informs the doctor there are no patients.
2. Otherwise, picks the next patient in line, prints their name for the doctor to call, and removes them from the queue.

## Program Flow (`main`)
A menu loop offering:
1. Add new patient (prompts for section, name, status)
2. Print all patients
3. Get next patient (prompts for section)
4. Exit

## Known Issues
- **Insert logic is swapped versus the spec.** The spec says: regular patients go to the *end* of the queue, urgent patients go to the *beginning*. In the current code:
  - `status == 0` (regular) does `lst.insert(0, ...)` -> goes to the **beginning** (should be the end).
  - `status == 1` (urgent) does `lst.append(...)` -> goes to the **end** (should be the beginning).

  This is backwards from the requirement and should be swapped: `status == 0` should `append`, `status == 1` should `insert(0, ...)`.

- **`pickup_patient` always pops from the end (`[-1]`).** Depending on how the insert logic above is fixed, "front of the line" may not correspond to index `-1`. Once the insert order is corrected (urgent at index 0, regular appended at the end), the doctor should pick up from index `0` (the front of the queue), not `-1`.

## Files
- `hospital_system.py` — full implementation
