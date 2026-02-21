class RunResult:
    def __init__(self, success: bool, message: str = ''):
        self.success = success
        self.message = message


def run_multi(functions, *args, **kwargs):
    results = []
    for func in functions:
        try:
            result = func(*args, **kwargs)
            results.append(RunResult(True, result))
        except Exception as e:
            results.append(RunResult(False, str(e)))
    return results