def get_meta(
    total: int,
    last_page: int,
    page: int,
    per_page: int
): 
    return {"total": total, "lastPage": last_page, "currentPage": page, "perPage": per_page}