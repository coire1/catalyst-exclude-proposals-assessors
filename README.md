# FeedbackChallenge tool backend

This repo contains a utility to get the assessors that are also proposers in Project Catalyst. These data are intended to be consumed by the QA scripts.

## Configuration

Install requirements with:

```
pip3 install -r requirements.txt
```

Copy `options.json.template` to `options.json` and set:

- `ideascale_api_token` the API token used to fect data from the Ideascale API.
- `ideascale_base_api_url` the Ideascale API base url, like
`https://cardano.ideascale.com/a/rest`
- `group_ids` the ids of user groups to query
- `members_endpoint` the endpoint to get `members`.
- `single_member_endpoint` the endpoint to get singular `member` info.


## Usage

Launch the script with:

```
python3 get-assessors-proposers.py
```

The output will be stored in `users.json`, a josn file with the list of users, proposalsIds and challengesIds
