#!/bin/bash

# Kill by process name as fallback
pkill -f "msg_MID360_launch" || true

exit 0