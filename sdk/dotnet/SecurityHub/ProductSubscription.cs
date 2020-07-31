// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.SecurityHub
{
    /// <summary>
    /// Subscribes to a Security Hub product.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleAccount = new Aws.SecurityHub.Account("exampleAccount", new Aws.SecurityHub.AccountArgs
    ///         {
    ///         });
    ///         var current = Output.Create(Aws.GetRegion.InvokeAsync());
    ///         var exampleProductSubscription = new Aws.SecurityHub.ProductSubscription("exampleProductSubscription", new Aws.SecurityHub.ProductSubscriptionArgs
    ///         {
    ///             ProductArn = current.Apply(current =&gt; $"arn:aws:securityhub:{current.Name}:733251395267:product/alertlogic/althreatmanagement"),
    ///         }, new CustomResourceOptions
    ///         {
    ///             DependsOn = 
    ///             {
    ///                 exampleAccount,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class ProductSubscription : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of a resource that represents your subscription to the product that generates the findings that you want to import into Security Hub.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The ARN of the product that generates findings that you want to import into Security Hub - see below.
        /// </summary>
        [Output("productArn")]
        public Output<string> ProductArn { get; private set; } = null!;


        /// <summary>
        /// Create a ProductSubscription resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ProductSubscription(string name, ProductSubscriptionArgs args, CustomResourceOptions? options = null)
            : base("aws:securityhub/productSubscription:ProductSubscription", name, args ?? new ProductSubscriptionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ProductSubscription(string name, Input<string> id, ProductSubscriptionState? state = null, CustomResourceOptions? options = null)
            : base("aws:securityhub/productSubscription:ProductSubscription", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ProductSubscription resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ProductSubscription Get(string name, Input<string> id, ProductSubscriptionState? state = null, CustomResourceOptions? options = null)
        {
            return new ProductSubscription(name, id, state, options);
        }
    }

    public sealed class ProductSubscriptionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the product that generates findings that you want to import into Security Hub - see below.
        /// </summary>
        [Input("productArn", required: true)]
        public Input<string> ProductArn { get; set; } = null!;

        public ProductSubscriptionArgs()
        {
        }
    }

    public sealed class ProductSubscriptionState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of a resource that represents your subscription to the product that generates the findings that you want to import into Security Hub.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The ARN of the product that generates findings that you want to import into Security Hub - see below.
        /// </summary>
        [Input("productArn")]
        public Input<string>? ProductArn { get; set; }

        public ProductSubscriptionState()
        {
        }
    }
}
