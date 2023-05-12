# Industrial Training Group 6

Link for the flight map GitHub repository: https://github.com/zhangwengame/Python-Flight-Map

Link for the OpenFlights website: https://openflights.org/data.html#airport

Link for the OpenFlights Github: https://github.com/jpatokal/openflights

Link for the OpenFlights Github (data): https://github.com/jpatokal/openflights/tree/master/data



**Use the airport database for the longitude, altitude and continent information!
Example:**



**507**,"London Heathrow Airport","London","United Kingdom","LHR","EGLL",**51.4706**,**-0.461941**,83,0,"E",**"Europe/London"**,"airport","OurAirports"

Use the following:

Index 0: Airport ID

Index 6: Latitude

Index 7: Longitude

Index 11: Timezone. Can be used to determine the continent 





**Use the route data database for the route information, aircraft type and stop over number! Example:**

BA,1355,SIN,**3316**,LHR,**507**,,**0**,**744**
> Hello

Use the following:

Index 3: departure airport ID

Index 5: arrival airport ID

Index 7: number of stopovers

Index 8: aircraft type


# Instruction on how to start the server:
1. Clone the repository
2. Open command line (terminal).
Using command line:
3. type "python --version" to check if you have python yet
4. install flask by typing "pip install flask" (python server package)
4. cd to the directory you cloned the repository
5. type "python -m app" to start the localhost server. You can access the web app on http://127.0.0.1:5000
To use Ngrok:
6. start ngrok.exe
7. type "ngrok http 5000"
You will be able to reach your localhost on internet using the link Ngrok gives you



## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://version.aalto.fi/gitlab/ailusa1/industrial-training-group-6.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://version.aalto.fi/gitlab/ailusa1/industrial-training-group-6/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)



***

