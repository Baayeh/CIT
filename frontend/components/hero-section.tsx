import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Clock, CheckSquare } from 'lucide-react';

export function HeroSection() {
  return (
    <div className="h-screen place-content-center relative overflow-hidden bg-background pt-12 md:pt-24">
      <div className="container relative">
        {/* Decorative Elements */}
        <div className="absolute left-4 top-1/4 md:left-20">
          <Card className="w-48 h-48 bg-yellow-100 rotate-[-6deg] p-4 shadow-lg">
            <div className="text-sm">
              Track customer issues and resolve them faster
            </div>
            <div className="absolute bottom-4 left-4">
              <CheckSquare className="h-6 w-6 text-blue-500" />
            </div>
          </Card>
        </div>

        <div className="absolute right-4 top-1/4 md:right-20">
          <Card className="w-48 bg-white p-4 rotate-[6deg] shadow-lg">
            <div className="flex items-center gap-2 mb-2">
              <Clock className="h-5 w-5" />
              <div className="font-medium">Today&apos;s Issues</div>
            </div>
            <div className="text-sm text-muted-foreground">
              3 pending responses
            </div>
          </Card>
        </div>

        {/* Main Content */}
        <div className="relative z-10 mx-auto max-w-3xl text-center">
          <h1 className="font-bold tracking-tight text-4xl sm:text-5xl md:text-6xl lg:text-7xl">
            Track and resolve
            <span className="block text-muted-foreground mt-2">
              customer issues faster
            </span>
          </h1>
          <p className="mt-6 text-lg text-muted-foreground">
            Efficiently manage customer issues and boost team productivity with
            our comprehensive tracking system.
          </p>
          <div className="mt-8 flex justify-center">
            <Button size="lg" className="text-base">
              Get free demo
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}
