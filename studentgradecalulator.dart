import 'package:flutter/material.dart';

void main() {
  runApp(const StudentGradeApp());
}

class StudentGradeApp extends StatelessWidget {
  const StudentGradeApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Student Grade Calculator',
      theme: ThemeData(
        primarySwatch: Colors.indigo,
        useMaterial3: true,
      ),
      home: const GradeCalculator(),
    );
  }
}

class GradeCalculator extends StatefulWidget {
  const GradeCalculator({super.key});

  @override
  State<GradeCalculator> createState() => _GradeCalculatorState();
}

class _GradeCalculatorState extends State<GradeCalculator> {
  final TextEditingController nameController = TextEditingController();
  final List<TextEditingController> markControllers = List.generate(
    5,
    (index) => TextEditingController(),
  );

  String result = '';
  String grade = '';
  double percentage = 0;
  int total = 0;

  void calculateGrade() {
    int sum = 0;
    bool valid = true;

    for (var controller in markControllers) {
      int? mark = int.tryParse(controller.text);

      if (mark == null || mark < 0 || mark > 100) {
        valid = false;
        break;
      }

      sum += mark;
    }

    if (!valid) {
      setState(() {
        result = 'Please enter valid marks between 0 and 100.';
        grade = '';
      });
      return;
    }

    double percent = sum / 5;

    String calculatedGrade;

    if (percent >= 90) {
      calculatedGrade = 'A+';
    } else if (percent >= 80) {
      calculatedGrade = 'A';
    } else if (percent >= 70) {
      calculatedGrade = 'B';
    } else if (percent >= 60) {
      calculatedGrade = 'C';
    } else if (percent >= 50) {
      calculatedGrade = 'D';
    } else {
      calculatedGrade = 'F';
    }

    setState(() {
      total = sum;
      percentage = percent;
      grade = calculatedGrade;
      result = percent >= 40 ? 'PASS' : 'FAIL';
    });
  }

  void clearAll() {
    nameController.clear();

    for (var controller in markControllers) {
      controller.clear();
    }

    setState(() {
      total = 0;
      percentage = 0;
      grade = '';
      result = '';
    });
  }

  Widget markField(String subject, TextEditingController controller) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 15),
      child: TextField(
        controller: controller,
        keyboardType: TextInputType.number,
        decoration: InputDecoration(
          labelText: '$subject Marks',
          hintText: 'Enter marks out of 100',
          prefixIcon: const Icon(Icons.school),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    nameController.dispose();

    for (var controller in markControllers) {
      controller.dispose();
    }

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Student Grade Calculator',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
        backgroundColor: Colors.indigo,
        foregroundColor: Colors.white,
      ),

      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),

        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [

            const Icon(
              Icons.school,
              size: 70,
              color: Colors.indigo,
            ),

            const SizedBox(height: 10),

            const Text(
              'Calculate Your Grade',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 25),

            TextField(
              controller: nameController,
              decoration: InputDecoration(
                labelText: 'Student Name',
                hintText: 'Enter student name',
                prefixIcon: const Icon(Icons.person),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
            ),

            const SizedBox(height: 25),

            markField('Mathematics', markControllers[0]),
            markField('Science', markControllers[1]),
            markField('English', markControllers[2]),
            markField('Computer', markControllers[3]),
            markField('Social Studies', markControllers[4]),

            const SizedBox(height: 10),

            ElevatedButton(
              onPressed: calculateGrade,
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.indigo,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(vertical: 16),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
              child: const Text(
                'CALCULATE GRADE',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),

            const SizedBox(height: 12),

            OutlinedButton(
              onPressed: clearAll,
              style: OutlinedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 16),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
              child: const Text(
                'CLEAR',
                style: TextStyle(fontSize: 16),
              ),
            ),

            const SizedBox(height: 25),

            if (result.isNotEmpty)
              Card(
                elevation: 5,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16),
                ),
                child: Padding(
                  padding: const EdgeInsets.all(20),

                  child: Column(
                    children: [

                      const Text(
                        'RESULT',
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                          color: Colors.indigo,
                        ),
                      ),

                      const SizedBox(height: 15),

                      Text(
                        nameController.text.isEmpty
                            ? 'Student'
                            : nameController.text,
                        style: const TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                        ),
                      ),

                      const SizedBox(height: 15),

                      Text(
                        'Total Marks: $total / 500',
                        style: const TextStyle(fontSize: 17),
                      ),

                      const SizedBox(height: 8),

                      Text(
                        'Percentage: ${percentage.toStringAsFixed(2)}%',
                        style: const TextStyle(fontSize: 17),
                      ),

                      const SizedBox(height: 8),

                      Text(
                        'Grade: $grade',
                        style: const TextStyle(
                          fontSize: 22,
                          fontWeight: FontWeight.bold,
                          color: Colors.indigo,
                        ),
                      ),

                      const SizedBox(height: 8),

                      Text(
                        result,
                        style: TextStyle(
                          fontSize: 22,
                          fontWeight: FontWeight.bold,
                          color: result == 'PASS'
                              ? Colors.green
                              : Colors.red,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
          ],
        ),
      ),
    );
  }
}
