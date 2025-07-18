#!/usr/bin/env python3
import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Use .get with fallback to 'N/A'
        filled_template = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key) if attendee.get(key) else "N/A"
            filled_template = filled_template.replace("{" + key + "}", value)

        # Write to output_X.txt
        output_filename = f"output_{i}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(filled_template)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")

