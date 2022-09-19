from flask import Flask, render_template
from flask_restful import Api, Resource
import csv

app = Flask(__name__)
api = Api(app)


class AppPerUser(Resource):
    def get(self, user_id):
        with open(".data/user_job_cand.csv") as userjob_file:

            userjobreader = csv.reader(userjob_file, delimiter=",")
            jobsid = []

            for row in userjobreader:
                if row[0] == user_id:
                    jobsid.append({"jobid": row[1]})
                else:
                    continue

        with open(".data/jobs.csv") as job_file:
            jobs = []
            jobreader = csv.reader(job_file, delimiter=",")
            for id in jobsid:
                for row in jobreader:
                    if row[0] == id.value:
                        jobs.append({"JobId": row[0], "Title": row[1]})
                    else:
                        continue

        return jobs


class UsersForJob(Resource):
    def get(self, job_id):

        with open(".data/user_job_cand.csv") as userjob_file:
            usersid = []

            userjobreader = csv.reader(userjob_file, delimiter=",")
            for row in userjobreader:
                if row[0] == job_id:
                    usersid.append({"userid": row[0]})
                else:
                    continue
        with open(".data/users.csv") as users_file:
            users = []
            for id in usersid:
                userreader = csv.reader(users_file, delimiter=",")
                for row in userreader:
                    if row[0] == id.value:
                        users.append(
                            {"UserId": row[0], "FirstName": row[1], "LastName": row[2]}
                        )
                    else:
                        continue
        return users


api.add_resource(UsersForJob, "/getApplicationPerJob/<int:job_id>")
api.add_resource(AppPerUser, "/getApplicationPerUser/<int:user_id>")
if __name__ == "__main__":
    app.run(debug=True)
