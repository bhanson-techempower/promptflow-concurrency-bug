# promptflow-concurrency-bug

Initialize an environment:

```bash
python -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

Restart VSCode if you had it open because the PF extension will be bugged on the first install.

Run the demo in batch mode:

```bash
python -m main
```

You will likely see an error like this:

> Flow path .../promptflow-concurrency-bug/sub_flow2/sub_flow3 does not exist.

There's extra code in this repo to ensure the issue is more reproducible, but it can be reproduced with:

- One input in batch mode
- One sub_flow
- Without the loop in run_sub_flow
- Two instances of run_sub_flow in the main flow
