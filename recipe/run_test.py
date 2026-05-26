import platform
from subprocess import call
import sys

COV_FAIL_UNDER = 95
COV_ARGS = ["coverage", "run", "--source=simpy", "--branch"]
OS = platform.system()
PYTEST_ARGS = [
    "-vv",
    "--tb=long",
    "--color=yes",
]
OS_ARGS = {
    # too slow for realtime tests
    "Darwin": ["-k", "not(test_rt)"],
    # test assumes POSIX paths... and is too slow
    "Windows": ["-k", "not(exception_chaining or test_rt)"],
}
REPORT_ARGS = [
    "coverage",
    "report",
    "--show-missing",
    "--skip-covered",
    f"--fail-under={COV_FAIL_UNDER}",
]

if __name__ == "__main__":
    sys.exit(
        call([*COV_ARGS, "-m", "pytest", *PYTEST_ARGS, *OS_ARGS.get(OS, [])])
        or (call(REPORT_ARGS) if OS == "Linux" else 0)
    )
