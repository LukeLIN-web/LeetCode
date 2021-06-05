package parallelProgram;
class MainDemo{	
        //static volatile int count = 1;
        static int count = 1;
        public static void main(String[] args) throws Exception {
            Thread thread= new Thread(() -> {
                while (count == 1);
                System.out.println("result");
            });
            thread.start();
            Thread.sleep(100);
            count++;
            System.out.println(count);
            thread.join();
        }
}
