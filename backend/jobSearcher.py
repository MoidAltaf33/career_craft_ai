import requests
import pandas as pd

class JobSearcher:
    @staticmethod
    def scrape_jobs(query, total_jobs):
        url = "https://jsearch.p.rapidapi.com/search"
        headers = {
            "X-RapidAPI-Key": "c786eac3d4mshb49a5b348d87934p13bd86jsn5f87ba1590de",
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
        }
        querystring = {
            "query": query,
            "page": "1",
            "num_pages": str((total_jobs + 9) // 10),  # Calculate number of pages needed
            "date_posted": "all"
        }

        job_data = []

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            data = response.json()
            jobs = data.get('data', [])

            for job in jobs:
                job_info = {
                    "Title": job["job_title"],
                    "Company": job["employer_name"],
                    "Description": job["job_description"],
                    "Location": f"{job['job_city']}, {job['job_state']}, {job['job_country']}",
                    "Source": job["job_publisher"],
                    "Link": job["job_google_link"]
                }
                job_data.append(job_info)

        df = pd.DataFrame(job_data)
        return df
