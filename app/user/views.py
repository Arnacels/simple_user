from typing import List

from fastapi import APIRouter, Depends, Request

from common.presenters.schemas import DefaultDeleteResponse
from .repository import UserRepository
from .import schemas

router = APIRouter()


@router.get('/')
def user_all(
        *,
        repository: UserRepository = Depends(UserRepository.build),
) -> List[schemas.User]:
    """
    List of users
    """
    return repository.fetch_all()


@router.post('/')
def user_create(
        *,
        user_in: schemas.InsertUser,
        request: Request,
        repository: UserRepository = Depends(UserRepository.build),
) -> schemas.User:
    """
    Create user
    """
    print(request.json())
    return repository.insert(user_in=user_in)


@router.get('/{pk}')
def user_detail(
        *,
        pk: int,
        repository: UserRepository = Depends(UserRepository.build),
) -> schemas.User:
    """
    Detail user
    """
    return repository.fetch_one(pk=pk)


@router.delete('/{pk}')
def user_remove(
        *,
        pk: int,
        repository: UserRepository = Depends(UserRepository.build),
) -> DefaultDeleteResponse:
    """
    Remove user
    """
    repository.delete(pk=pk)
    return DefaultDeleteResponse()


@router.delete('/email/{email}')
def user_remove_by_email(
        *,
        email: str,
        repository: UserRepository = Depends(UserRepository.build),
) -> DefaultDeleteResponse:
    """
    Remove user by email
    """
    repository.delete_by_email(email=email)
    return DefaultDeleteResponse()


@router.put('/{pk}')
def user_update(
        *,
        pk: int,
        user_in: schemas.UpdateUser,
        repository: UserRepository = Depends(UserRepository.build),
) -> DefaultDeleteResponse:
    """
    Update user
    """
    repository.update_one(pk=pk, user_in=user_in)
    return DefaultDeleteResponse()
