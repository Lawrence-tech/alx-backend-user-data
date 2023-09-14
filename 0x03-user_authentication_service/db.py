#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base
from user import User  # Import the User model


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): User's email.
            hashed_password (str): Hashed password.

        Returns:
            User: The created User object.
        """
        # Create a new User instance
        new_user = User(email=email, hashed_password=hashed_password)

        # Add the user to the session
        self._session.add(new_user)

        # Commit the changes to the database
        self._session.commit()

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user in the database by the specified keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments to filter the query.

        Returns:
            User: The User object that matches the query.

        Raises:
            NoResultFound: If no results are found.
            InvalidRequestError: If invalid query arguments are passed.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound("No user found for the given criteria")
            return user
        except InvalidRequestError as e:
            raise InvalidRequestError("Invalid query arguments") from e
