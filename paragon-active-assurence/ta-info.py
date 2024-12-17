import requests
import json
import csv
import time
import datetime

url_system_status = "https://control-center/rest/accounts/lab/test_agents/"
headers = {"API-Token": "Ippm2IpXNCHlGvYMRGLGAIP2rQb6m7hrjVZI2Jm2"}

agent_list = []


def pull_info():
    response = requests.get(url_system_status, verify=False, headers=headers).json()
    with open('agents_jnpr-edu.json', 'w') as config_file:
        json.dump(response, config_file, indent=4)
    with open('agents_jnpr-edu.json', 'r') as config_file:
        data = json.load(config_file)
        agents = data['items']

    for agents in agents:
        agent_states = (agents['name'], agents['online'], datetime.datetime.utcnow())
        print(agent_states)
        agent_list.append(agent_states)
        print(agent_list)


def create_csv_agents():
    with open('agents_jnpr-edu.csv', 'w') as csv_agent:
        fieldnames = ['Agent Name', 'State', 'Timestamp']
        file = csv.DictWriter(csv_agent, fieldnames=fieldnames)
        file.writeheader()
        file = csv.writer(csv_agent, delimiter=',',
                          quotechar='|', quoting=csv.QUOTE_NONE)
        for agent_lists in agent_list:
            file.writerow(agent_lists)


if __name__ == '__main__':
    while True:
        agent_info = pull_info()
        create_csv_agents()
        time.sleep(10)
