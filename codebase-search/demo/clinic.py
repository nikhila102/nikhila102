"""Fictional scheduling examples for evaluating source retrieval."""


def cancel_appointment(appointment):
    """Release the time slot when a patient cancels an appointment."""
    return {**appointment, "status": "cancelled"}


def get_waitlist(clinic, patients):
    """Find patients waiting for an opening at the clinic."""
    return [patient for patient in patients if patient["clinic"] == clinic]


def reminder_message(patient):
    """Compose a reminder before the scheduled visit."""
    return f"Hi {patient}, your visit is tomorrow."
