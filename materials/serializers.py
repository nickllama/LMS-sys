from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    quantity_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True, many=True)
    def get_quantity_lessons(self, obj):
        quantity_lessons = obj.lesson.all().count()

        if not quantity_lessons:
            return None
        else:
            return quantity_lessons

    class Meta:
        model = Course
        fields = '__all__'
