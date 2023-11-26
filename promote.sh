#!/bin/bash

# Function to display usage message
usage() {
  echo "Usage: promote.sh --model_name <model_name> --model_version <model_version> --status <Staging|Production|Archived> [--test-set <test_set>]"
  exit 1
}

# Parse the arguments
while [[ $# -gt 0 ]]; do
  key="$1"

  case $key in
    --model_name)
      MODEL_NAME="$2"
      shift
      shift
      ;;
    --model_version)
      MODEL_VERSION="$2"
      shift
      shift
      ;;
    --status)
      STATUS="$2"
      shift
      shift
      ;;
    --test-set)
      TEST_SET="$2"
      shift
      shift
      ;;
    *)
      usage
      ;;
  esac
done

# Check if the required arguments are present
if [ -z "$MODEL_NAME" ] || [ -z "$MODEL_VERSION" ] || [ -z "$STATUS" ]; then
  usage
fi

# Export variables as environment variables
export TEST_MODEL_NAME="$MODEL_NAME"
export TEST_MODEL_VERSION="$MODEL_VERSION"
export TEST_FILE="$TEST_SET"
export TEST_TEST_TEST=0.9

echo "Running promote command..."
promote -i $TEST_SET -m $TEST_MODEL_NAME -v $MODEL_VERSION -s $STATUS
