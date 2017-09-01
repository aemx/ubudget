<img src = "https://www.dropbox.com/s/70f6rflcanagapl/ubudget.png?raw=1" alt = "ubudget" style = "width: 400px; display: block; margin: auto"/>

<p style = "text-align: center;">An ultra-minimal budgeting program written in Python.</p>

## Setup

### Requirements
- A UNIX-like operating system (Linux, macOS)
- Python 3.6+
- `curl` or `wget`
- [Robpol86's](https://github.com/Robpol86) [`terminaltables`](https://github.com/Robpol86/terminaltables) module

### Installation

To install μbudget, use `curl` or `wget` within your desired installation directory.

with `curl`:

```
sudo curl -L https://github.com/aemx/ubudget/archive/0.0.1.tar.gz -o 0.0.1.tar.gz
sudo tar -xzf 0.0.1.tar.gz && sudo rm -r 0.0.1.tar.gz
```

with `wget`:

```
sudo wget https://github.com/aemx/ubudget/archive/0.0.1.tar.gz -O 0.0.1.tar.gz
sudo tar -xzf 0.0.1.tar.gz && sudo rm -r 0.0.1.tar.gz
```

## Using μbudget

### Running for the first time

An example dataset named [`data.json`](https://github.com/aemx/ubudget/blob/master/data.json) is provided with all copies of μbudget. To test this dataset, run `python ubudget.py` from within the `ubudget-0.0.1/` directory.  
Your output should look something like this:

<img src = "https://www.dropbox.com/s/oxlwni8nkuep78r/sampletable.png?raw=1" alt = "sampletable"/>

If this is not the case, please open an issue and describe the problem [**here**](https://github.com/robbyrussell/oh-my-zsh/issues).

### Adding your own data

Within the [`data.json`](https://github.com/aemx/ubudget/blob/master/data.json) file are two lists, `"p"` and `"t"`.
- The `"p"` (percentages) array contains three values, representing a percentage of money to _save_, _spend_, and keep for _emergencies_.
- The `"t"` (transactions) array contains four arrays, `"n"`, `"d"`, `"t"`, and `"a"`.
    - The `"n"` array represents a name for your transaction. This should be around _10 characters_, but is unlimited.
    - The `"d"` array represents an ISO 8601 date for your transaction. This should be in a _%Y-%m-%d_ format.
    - The `"t"` array represents a transaction type. This _**MUST**_ be either a case-sensitive _D_ for _deposit_ or _W_ for _withdrawal_.
    - The `"a"` array represents an amount. This _**MUST**_ be a _float_ value.

## Uninstallation

To uninstall μbudget, simply type the following from within the directory containing `ubudget-0.0.1/`:
```
sudo rm -r ubudget-0.0.1
```

## License

This project is licensed under the [MIT License](https://github.com/aemx/ubudget/blob/master/LICENSE).
  
---
_<p style = "text-align: center;">Last updated on 2017 September 01 for version 0.0.1</p>_