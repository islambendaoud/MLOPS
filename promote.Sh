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
export TEST_STATUS="$STATUS"
export TEST_TEST_TEST=0.9


pytest_output=$(pytest pkg_resources.resource_filename('sentiment_analyzer', "./tests"))

#
# Check the status and perform corresponding actions
case $STATUS in
  "Staging")
    echo "Promoting to Staging..."
    # Add commands for promotion to Staging
    ;;
  "Production")
    if [ -z "$TEST_SET" ]; then
      echo "Error: Test set is required for promotion to Production."
      usage
    fi
    echo "Promoting to Production with test set: $TEST_SET"
    # Add commands for promotion to Production
    ;;
  "Archived")
    echo "Archiving the model..."
    # Add commands for archiving the model
    ;;
  *)
    echo "Error: Invalid status. Status must be one of Staging, Production, or Archived."
    usage
    ;;
esac

# Add commands common to all promotions, if necessary
echo "Promotion complete."
