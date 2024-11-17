
from django.shortcuts import render
from .models import JobListing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs(request):
    if request.method == 'POST':
        resume = request.POST['resume']
        
        # Retrieve job listings from the database
        jobs = JobListing.objects.all()
        
        # Combine job details for TF-IDF processing
        job_descriptions = [
            f"{job.title} {job.description} {job.skills}" for job in jobs
        ]
        
        # TF-IDF vectorization
        tfidf = TfidfVectorizer()
        job_vectors = tfidf.fit_transform(job_descriptions)
        resume_vector = tfidf.transform([resume])
        
        # Calculate similarity scores
        similarity_scores = cosine_similarity(resume_vector, job_vectors).flatten()
        
        # Attach similarity scores to jobs
        recommendations = [
            (job, score) for job, score in zip(jobs, similarity_scores)
        ]
        
        # Sort by similarity scores
        recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)[:3]
        
        return render(request, 'results.html', {'recommendations': recommendations})
    
    return render(request, 'index.html')
