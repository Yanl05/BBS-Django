
models.employee.objects.values("dept").\
    annotate(avg=Avg("salary")).values("dept", "avg")