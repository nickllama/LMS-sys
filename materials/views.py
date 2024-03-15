from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    default_serializer = CourseSerializer
    queryset = Course.objects.all()
    serializers_choice = {
        'retrieve': CourseSerializer,
    }

    def get_serializer_class(self):
        return self.serializers_choice.get(self.action, self.default_serializer)


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class LessonCreateApiView(generics.CreateAPIView):
    serializer_class = LessonSerializer
