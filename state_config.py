"""
State configuration for this GeorgiaDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "GA"
STATE_NAME = "Georgia"
APP_NAME = "GeorgiaDischargeWatch"
APP_TAGLINE = "Georgia Discharge Monitoring"
DOMAIN = "georgiadischargewatch.org"
DATA_FILE = "ga_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@georgiadischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "EST"
EPA_REGION = 4
