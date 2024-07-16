# There's no public way to override this. The default value is 2 in batch mode.
# Setting it to 1 does prevent the concurrency issue from happening.
# import promptflow.executor._line_execution_process_pool as _line_execution_process_pool
# _line_execution_process_pool.DEFAULT_CONCURRENCY_BULK = 1

from promptflow.client import PFClient


def main():
    pf = PFClient()
    results = pf.run(
        flow=".",
        data="data.jsonl",
        column_mapping={"name": "${data.name}"},
        environment_variables={
            "PF_WORKER_COUNT": "3",
        },
    )
    print(results)


if __name__ == "__main__":
    main()
