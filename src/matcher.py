def calculate_match(cv_skills, job_skills):
    cv = set(cv_skills)  # set() - A halmaz nem tartalmaz duplikációt
    job = set(job_skills)

    common = cv.intersection(job)  # intersection() - Közös elemek
    total = cv.union(job)  # union() - Összes egyedi elem

    if len(total) == 0:
        return 0
    
    return round(len(common) / len(total) * 100, 2)