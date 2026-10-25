
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone

from .models import Note
from .forms import NoteForm


@login_required
def note_list(request):
    notes = Note.objects.filter(
        created_by=request.user
    ).select_related("created_by").order_by("-created_at")

    return render(
        request,
        "notes/note_list.html",
        {"notes": notes}
    )


@login_required
def note_create(request):
    form = NoteForm(request.POST or None)

    if form.is_valid():
        note = form.save(commit=False)
        note.created_by = request.user
        note.save()

        return redirect("note_list")

    return render(
        request,
        "notes/note_form.html",
        {"form": form, "title": "New Note"}
    )


@login_required
def note_update(request, pk):
    note = get_object_or_404(
        Note,
        pk=pk,
        created_by=request.user
    )

    form = NoteForm(request.POST or None, instance=note)

    if form.is_valid():
        note = form.save(commit=False)
        note.created_by = request.user
        note.save()

        return redirect("note_list")

    return render(
        request,
        "notes/note_form.html",
        {"form": form, "title": "Edit Note"}
    )


@login_required
def note_delete(request, pk):
    note = get_object_or_404(
        Note,
        pk=pk,
        created_by=request.user
    )

    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(
        request,
        "notes/note_confirm_delete.html",
        {"note": note}
    )


# AJAX endpoint: returns the latest notes as JSON.
@login_required
def notes_data(request):
    notes = Note.objects.filter(
        created_by=request.user
    ).select_related("created_by").order_by("-created_at")

    data = [
        {
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "is_done": note.is_done,
            "created_by": note.created_by.username,
            "created_at": timezone.localtime(
                note.created_at
            ).strftime("%b %d, %Y %H:%M"),
            "created_day": note.created_day or "",
            "update_url": f"/update/{note.id}/",
            "delete_url": f"/delete/{note.id}/",
        }
        for note in notes
    ]

    return JsonResponse({"notes": data})




