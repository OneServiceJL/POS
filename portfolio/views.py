from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactMessageForm
from .models import Education, Experience, Profile, Project, Skill


def home(request):
    profile = Profile.objects.first()
    if profile is None:
        profile = Profile(
            full_name="Your Name",
            title="Portfolio & CV Manager",
            summary="A sample Django CV and portfolio site with skills, experience, education, projects, and contact messaging.",
            email="you@example.com",
            phone="+1234567890",
            location="Anytown, Anywhere",
            website="https://example.com",
            linkedin="https://linkedin.com",
            github="https://github.com",
        )

    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    projects = Project.objects.filter(show_in_portfolio=True)
    form = ContactMessageForm()

    return render(
        request,
        "portfolio/home.html",
        {
            "profile": profile,
            "skills": skills,
            "experiences": experiences,
            "education": education,
            "projects": projects,
            "form": form,
        },
    )


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "portfolio/project_detail.html", {"project": project})


def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_success")
    else:
        form = ContactMessageForm()

    return render(request, "portfolio/contact.html", {"form": form})


def contact_success(request):
    return render(request, "portfolio/contact_success.html")
