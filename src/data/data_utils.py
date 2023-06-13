import re
import logging
from tqdm import tqdm
import nltk
from data.utils.tqdm_logger import TqdmToLogger

logger = logging.getLogger(__name__)
tqdm_out = TqdmToLogger(logger,level=logging.INFO)

STRING_MATCHING_PATTERN = re.compile(r'([bruf]*)(\"\"\"|\'\'\'|\"|\')(?:(?!\2)(?:\\.|[^\\]))*\2')
NON_SPACE_MATCHING_PATTERN = re.compile(r'\S')

def load_lines(path):
    """
    Load lines from given path.

    Args:
        path (str): Dataset file path

    Returns:
        list: List of lines

    """
    with open(path, encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    return lines


def parse_for_code2code(buggy_path, fixed_path):
    """
    Load and parse for bug fix.

    Args:
        buggy_path (str): Path of buggy code
        fixed_path (str): Path of fixed code

    Returns:
        (list[str], list[str], list[str], list[str]):
            - List of strings: source code
            - List of strings: AST sequence
            - List of strings: name sequence
            - List of strings: target code

    """
    buggy_lines = load_lines(buggy_path)
    fixed_lines = load_lines(fixed_path)
    assert len(buggy_lines) == len(fixed_lines)
    codes = []
    targets = []
    for buggy, fixed in tqdm(zip(buggy_lines, fixed_lines), desc='Parsing', total=len(buggy_lines)):
        try:
            codes.append(buggy.lower())
            targets.append(fixed.lower())
        except Exception:
            continue
    return codes, targets
