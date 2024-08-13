def get_value(data, key, default, lookup=None, mapper=None):
    """
    Finds the value from data associated with key, or default if the
    key isn't present.
    If a lookup enum is provided, this value is then transformed to its
    enum value.
    If a mapper function is provided, this value is then transformed
    by applying mapper to it.
    """
    # Consider using .get() to handle cases where the key might not exist in the dictionary
    return_value = data.get(key, default)

    # The check for None and empty string can be consolidated to make the code cleaner
    if not return_value:
        return_value = default

    # Adding check in case lookup dictionary is empty
    if lookup:
        return_value = lookup.get(return_value, return_value)  # Fallback to return_value if not found in lookup

    # Check if mapper is callable before applying it
    if mapper and callable(mapper):
        return_value = mapper(return_value)

    return return_value



def ftp_file_prefix(namespace):
    """
    Given a namespace string with dot-separated tokens, returns the
    string with the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """
    # Ensure the namespace string is not empty and has at least one dot
    if not namespace or '.' not in namespace:
        raise ValueError("Namespace must be a non-empty string with at least one dot.")

    return ".".join(namespace.split(".")[:-1]) + '.ftp'


print(ftp_file_prefix("a.b.c"))


def string_to_bool(string):
    """
    Returns True if the given string is 'true' case-insensitive,
    False if it is 'false' case-insensitive.
    Raises ValueError for any other input.
    """
    # Consider using a dictionary for better readability
    true_values = {'true'}
    false_values = {'false'}

    # Simplify the conditional checks by using the sets defined above
    lowered_string = string.lower()
    if lowered_string in true_values:
        return True
    if lowered_string in false_values:
        return False

    raise ValueError(f'String {string} is neither true nor false')





# Define constants for dictionary keys to avoid hardcoding strings
NAMESPACE_KEY = 'Namespace'
AIRFLOW_DAG_KEY = 'Airflow DAG'
AVAILABLE_START_TIME_KEY = 'Available Start Time'
AVAILABLE_END_TIME_KEY = 'Available End Time'
REQUIRES_SCHEMA_MATCH_KEY = 'Requires Schema Match'
SCHEDULE_KEY = 'Schedule'
DELTA_DAYS_KEY = 'Delta Days'
FILE_NAMING_PATTERN_KEY = 'File Naming Pattern'
FTP_FILE_PREFIX_KEY = 'FTP File Prefix'

#Example of a DeltaDays

DeltaDays = {
    'DAY_BEFORE': 1,
    'DAY_OF': 0,
    'DAY_AFTER': -1
}


def config_from_dict(config_dict):
    """
    Given a dict representing a row from a namespaces CSV file,
    returns a DAG configuration as a pair whose first element is the
    DAG name and whose second element is a dict describing the DAG's properties.
    """
    # Use get with default values to handle missing keys
    namespace = config_dict.get(NAMESPACE_KEY, "")
    if not namespace:
        raise ValueError(f"Missing or empty value for key: {NAMESPACE_KEY}")

    return (
        config_dict.get(AIRFLOW_DAG_KEY, "default_dag_name"),
        {
            "earliest_available_delta_days": 0,
            "lif_encoding": 'json',
            "earliest_available_time": get_value(
                config_dict, AVAILABLE_START_TIME_KEY, '07:00'
            ),
            "latest_available_time": get_value(
                config_dict, AVAILABLE_END_TIME_KEY, '08:00'
            ),
            "require_schema_match": get_value(
                config_dict, REQUIRES_SCHEMA_MATCH_KEY, 'True', mapper=string_to_bool
            ),
            "schedule_interval": get_value(
                config_dict, SCHEDULE_KEY, '1 7 * * * '
            ),
            "delta_days": get_value(
                config_dict, DELTA_DAYS_KEY, 'DAY_BEFORE', lookup=DeltaDays
            ),
            "ftp_file_wildcard": get_value(
                config_dict, FILE_NAMING_PATTERN_KEY, None
            ),
            "ftp_file_prefix": get_value(
                config_dict, FTP_FILE_PREFIX_KEY, ftp_file_prefix(namespace)
            ),
            "namespace": namespace,
        }
    )
