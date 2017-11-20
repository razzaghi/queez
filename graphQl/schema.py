import graphene

from graphene_django.types import DjangoObjectType

from . import models


class categoryType(DjangoObjectType):
    class Meta:
        model = models.category


class questionType(DjangoObjectType):
    class Meta:
        model = models.question


class optionType(DjangoObjectType):
    class Meta:
        model = models.option


class storyType(DjangoObjectType):
    class Meta:
        model = models.story


class Query(graphene.AbstractType):
    all_categories = graphene.List(categoryType)
    all_questions = graphene.List(questionType)
    all_options = graphene.List(optionType)
    all_stories = graphene.List(storyType)
    category = graphene.Field(categoryType, id=graphene.Int())
    question = graphene.List(questionType, category=graphene.String())
    story = graphene.Field(storyType, category=graphene.String(), id=graphene.Int())

    def resolve_all_questions(self, info, *kargs, **kwargs):
        return models.question.objects.all()

    def resolve_all_categories(self, info, *kargs, **kwargs):
        return models.category.objects.all()

    def resolve_all_options(self, info, *kargs, **kwargs):
        return models.option.objects.all()

    def resolve_all_stories(self, info, *kargs, **kwargs):
        return models.story.objects.all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return models.category.objects.get(pk=id)
        return None

    def resolve_question(self, info, **kwargs):
        category = kwargs.get('category')
        if category is not None:
            return models.question.objects.filter(category__name=category)
        return None

    def resolve_story(self, info, **kwargs):
        category = kwargs.get('category')
        id = kwargs.get('id')
        if category is not None:
            return models.story.objects.get(category__name=category)
        if id is not None:
            return models.story.objects.get(pk=id)
        return None
